#!/usr/bin/env python3
"""Find nonce from Elementor editor and get revisions"""
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

# Try multiple nonce patterns
patterns = [
    r'"ajax":\{"nonce":"([^"]+)"',
    r'\"ajax\":\{[^}]*\"nonce\":\"([^\"]+)\"',
    r'elementorCommon.*?"nonce":"([a-f0-9]+)"',
    r'"nonce"\s*:\s*"([a-f0-9]{10})"',
    r'wp\.apiFetch.*?nonce.*?"([a-f0-9]{10})"',
]
ajax_nonce = None
for p in patterns:
    m = re.search(p, ed_html)
    if m:
        ajax_nonce = m.group(1)
        print(f"Found nonce via pattern '{p[:40]}': {ajax_nonce}")
        break

if not ajax_nonce:
    # Look for any 10-char hex that could be a nonce
    nonces = re.findall(r'"nonce":"([a-f0-9]{10})"', ed_html)
    print(f"All nonces found: {nonces}")
    if nonces:
        ajax_nonce = nonces[0]

print(f"Using nonce: {ajax_nonce}")

# Get WP revisions via admin AJAX - standard WP revisions
wp_nonce_match = re.search(r'nonce.*?["\']([a-f0-9]{10})["\']', ed_html)
print(f"WP nonce match: {wp_nonce_match.group(1) if wp_nonce_match else 'none'}")

# Get list of all WP post revisions from admin
revisions_url = f'https://brainyogaacademy.com/wp-admin/revision.php?action=list&post_id=1111'
req3 = urllib.request.Request(revisions_url, headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req3) as r3:
    rev_html = r3.read().decode('utf-8')

# Find revision IDs in the response
rev_ids = re.findall(r'revision[_-](\d+)', rev_html)
rev_ids_2 = re.findall(r'post=(\d+).*?revision', rev_html)
print(f"\nRevision IDs found (method 1): {rev_ids[:20]}")
print(f"Revision IDs found (method 2): {rev_ids_2[:20]}")

# Save snippet for inspection
with open('/tmp/rev_html_snippet.txt', 'w') as f:
    f.write(rev_html[:5000])
print("\nRevision HTML saved to /tmp/rev_html_snippet.txt")
