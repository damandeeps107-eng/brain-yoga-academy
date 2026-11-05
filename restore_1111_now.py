#!/usr/bin/env python3
"""
Restore Post 1111 from revision 1248 (2 days ago = clean original children page)
using Elementor's restore_revision AJAX action.
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

# Load the good elements from revision 1248
with open('/tmp/rev_1248_elements.json', 'r') as f:
    good_elements = json.load(f)
print(f"Loaded {len(good_elements)} good elements from revision 1248")

# Check if there's already a bottom bar in the good elements (there shouldn't be)
el_str = json.dumps(good_elements)
has_bar = "by_bottom_adult_bar" in el_str or "by-bottom-adult-bar" in el_str
print(f"Has our bottom bar: {has_bar}")

# Save back to Post 1111 using save_builder
actions = {
    'save_builder': {
        'action': 'save_builder',
        'data': {
            'status': 'publish',
            'elements': good_elements
        }
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
    res = json.loads(r.read().decode())
    save_result = res.get('data', {}).get('responses', {}).get('save_builder', {})
    print(f"\n✅ Post 1111 RESTORED! save_builder success: {save_result.get('success')}")

# Purge LiteSpeed cache
print("\nPurging LiteSpeed cache...")
admin_page = opener.open(urllib.request.Request('https://brainyogaacademy.com/wp-admin/', headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf-8')
ls_nonce_match = re.search(r'LSCWP_NONCE=([a-f0-9]+)', admin_page)
ls_nonce = ls_nonce_match.group(1) if ls_nonce_match else '663a0c4afd'

purge_url = f'https://brainyogaacademy.com/?LSCWP_CTRL=purge&LSCWP_NONCE={ls_nonce}&litespeed_type=purge_all'
try:
    req3 = urllib.request.Request(purge_url, headers={'User-Agent': 'Mozilla/5.0', 'Referer': 'https://brainyogaacademy.com/wp-admin/'})
    with opener.open(req3) as r3:
        print(f"✅ LiteSpeed cache purged! Status: {r3.status}")
except Exception as e:
    print(f"Cache purge: {e}")

print("\n🎉 Done! Children page should be RESTORED now!")
print("Check: https://brainyogaacademy.com/")
