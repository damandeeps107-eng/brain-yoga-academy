#!/usr/bin/env python3
"""Restore Post 1111 from its latest WP revision (before our wipe)"""
import urllib.request, urllib.parse, http.cookiejar, ssl, json, re

ctx = ssl._create_unverified_context()
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), urllib.request.HTTPSHandler(context=ctx))

# Login
login_data = urllib.parse.urlencode({
    'log': 'rajendraboddu@gmail.com',
    'pwd': 'Gemini#1979',
    'wp-submit': 'Log In',
    'redirect_to': 'https://brainyogaacademy.com/wp-admin/',
    'testcookie': '1'
}).encode()
opener.open(urllib.request.Request('https://brainyogaacademy.com/wp-login.php', data=login_data, headers={'User-Agent': 'Mozilla/5.0'}))
print("Logged in!")

# Get all revisions of Post 1111
req = urllib.request.Request(
    'https://brainyogaacademy.com/wp-json/wp/v2/pages/1111/revisions?per_page=20',
    headers={'User-Agent': 'Mozilla/5.0'}
)
with opener.open(req) as r:
    revisions = json.loads(r.read().decode())

print(f"Found {len(revisions)} revisions")
for i, rev in enumerate(revisions):
    rev_id = rev.get('id')
    date = rev.get('date', 'unknown')
    el_data = rev.get('meta', {}).get('_elementor_data', '[]') if rev.get('meta') else '[]'
    if isinstance(el_data, str):
        try:
            el_count = len(json.loads(el_data)) if el_data else 0
        except:
            el_count = -1
    else:
        el_count = len(el_data) if el_data else 0
    print(f"  [{i}] rev_id={rev_id} date={date} elementor_elements={el_count}")

# Find best revision (most elements, not the wiped one)
best_rev = None
best_count = 0
for rev in revisions:
    el_data = rev.get('meta', {}).get('_elementor_data', '[]') if rev.get('meta') else '[]'
    if isinstance(el_data, str):
        try:
            el_list = json.loads(el_data) if el_data else []
        except:
            el_list = []
    else:
        el_list = el_data or []
    if len(el_list) > best_count:
        best_count = len(el_list)
        best_rev = rev

if best_rev and best_count > 0:
    print(f"\nBest revision: id={best_rev['id']}, elements={best_count}")
    best_el_data = best_rev.get('meta', {}).get('_elementor_data', '[]') if best_rev.get('meta') else '[]'
    if isinstance(best_el_data, str):
        best_elements = json.loads(best_el_data)
    else:
        best_elements = best_el_data
    
    # Save these elements back to Post 1111
    print("Restoring via WP REST API...")
    restore_data = json.dumps({
        'meta': {'_elementor_data': json.dumps(best_elements)}
    }).encode()
    req2 = urllib.request.Request(
        'https://brainyogaacademy.com/wp-json/wp/v2/pages/1111',
        data=restore_data,
        method='POST',
        headers={'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/json'}
    )
    with opener.open(req2) as r2:
        result = json.loads(r2.read().decode())
        print(f"REST restore result status: {result.get('status')}")
else:
    print("\nNo good revision found via REST API — trying Elementor revision approach")
