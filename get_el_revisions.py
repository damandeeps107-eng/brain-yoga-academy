#!/usr/bin/env python3
"""
Get Elementor revisions and restore Post 1111 from last good revision.
Uses Elementor's get_revisions AJAX action.
"""
import urllib.request, urllib.parse, http.cookiejar, ssl, json, re

ctx = ssl._create_unverified_context()
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), urllib.request.HTTPSHandler(context=ctx))

login_data = urllib.parse.urlencode({
    'log': 'rajendraboddu@gmail.com', 'pwd': 'Gemini#1979',
    'wp-submit': 'Log In', 'redirect_to': 'https://brainyogaacademy.com/wp-admin/', 'testcookie': '1'
}).encode()
opener.open(urllib.request.Request('https://brainyogaacademy.com/wp-login.php', data=login_data, headers={'User-Agent': 'Mozilla/5.0'}))
print("Logged in!")

el_url = 'https://brainyogaacademy.com/wp-admin/post.php?post=1111&action=elementor'
req = urllib.request.Request(el_url, headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    ed_html = resp.read().decode('utf-8')

ajax_nonce = re.search(r'\"ajax\":\{[^}]*\"nonce\":\"([^\"]+)\"', ed_html).group(1)
print(f"Nonce: {ajax_nonce}")

# Try Elementor's get_revisions action
actions = {
    'get_revisions': {
        'action': 'get_revisions',
        'data': {'id': '1111'}
    }
}
ajax_data = urllib.parse.urlencode({
    'action': 'elementor_ajax',
    '_nonce': ajax_nonce,
    'editor_post_id': '1111',
    'actions': json.dumps(actions)
}).encode()

req2 = urllib.request.Request(
    'https://brainyogaacademy.com/wp-admin/admin-ajax.php',
    data=ajax_data,
    headers={'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/x-www-form-urlencoded'}
)
with opener.open(req2) as r:
    raw = r.read().decode('utf-8')

print(f"\nRaw response (first 2000 chars):\n{raw[:2000]}")

# Try to get WP revisions from the post's autosave/revision posts
# via WP admin AJAX
wp_nonce = re.search(r'"nonce":"([a-f0-9]{10})"', ed_html)
if wp_nonce:
    wp_nonce_val = wp_nonce.group(1)
    print(f"\nWP nonce: {wp_nonce_val}")
    
    # Try wp_revisions_to_keep
    revisions_check = urllib.parse.urlencode({
        'action': 'get-revision',
        '_wpnonce': wp_nonce_val,
        'post_id': '1111'
    }).encode()
    
    req3 = urllib.request.Request(
        'https://brainyogaacademy.com/wp-admin/admin-ajax.php',
        data=revisions_check,
        headers={'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/x-www-form-urlencoded'}
    )
    try:
        with opener.open(req3) as r3:
            print(f"\nRevision AJAX: {r3.read().decode()[:500]}")
    except Exception as e:
        print(f"Revision AJAX error: {e}")
