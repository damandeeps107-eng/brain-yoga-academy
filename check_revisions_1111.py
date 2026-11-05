#!/usr/bin/env python3
"""
Restore Post 1111 children page from Elementor revision history.
Uses Elementor's own revision system via WP admin.
"""
import urllib.request, urllib.parse, http.cookiejar, ssl, json, re

ctx = ssl._create_unverified_context()
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), urllib.request.HTTPSHandler(context=ctx))

# 1. Login
login_data = urllib.parse.urlencode({
    'log': 'rajendraboddu@gmail.com',
    'pwd': 'Gemini#1979',
    'wp-submit': 'Log In',
    'redirect_to': 'https://brainyogaacademy.com/wp-admin/',
    'testcookie': '1'
}).encode()
opener.open(urllib.request.Request('https://brainyogaacademy.com/wp-login.php', data=login_data, headers={'User-Agent': 'Mozilla/5.0'}))
print("✅ Logged in!")

# 2. Get Elementor editor page for Post 1111 to get nonce
el_url = 'https://brainyogaacademy.com/wp-admin/post.php?post=1111&action=elementor'
req = urllib.request.Request(el_url, headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    ed_html = resp.read().decode('utf-8')

ajax_nonce = re.search(r'"ajax":\{"nonce":"([^"]+)"', ed_html).group(1)
print(f"✅ Got Elementor nonce: {ajax_nonce}")

# 3. Get Elementor revision history for Post 1111
actions_get_revisions = {
    'get_revisions': {
        'action': 'get_revisions',
        'data': {
            'id': '1111'
        }
    }
}
ajax_data = urllib.parse.urlencode({
    'action': 'elementor_ajax',
    '_nonce': ajax_nonce,
    'editor_post_id': '1111',
    'actions': json.dumps(actions_get_revisions)
}).encode()

req2 = urllib.request.Request(
    'https://brainyogaacademy.com/wp-admin/admin-ajax.php',
    data=ajax_data,
    headers={'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/x-www-form-urlencoded'}
)
with opener.open(req2) as r:
    rev_response = json.loads(r.read().decode())

revisions_data = rev_response.get('data', {}).get('responses', {}).get('get_revisions', {})
print(f"\nRevision response success: {revisions_data.get('success')}")

# Check for revisions
revisions = revisions_data.get('data', []) if revisions_data.get('success') else []

# Try alternate path
if not revisions:
    revisions = rev_response.get('data', {}).get('revisions', [])

print(f"Found {len(revisions)} Elementor revisions")

for i, rev in enumerate(revisions[:10]):
    rev_id = rev.get('id', rev.get('ID'))
    date = rev.get('date', rev.get('post_date', 'unknown'))
    print(f"  [{i}] id={rev_id} date={date}")

# Save response for inspection
with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/rev_response_1111.json', 'w') as f:
    json.dump(rev_response, f, indent=2)
print("\nFull response saved to rev_response_1111.json")
