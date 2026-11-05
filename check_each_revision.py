#!/usr/bin/env python3
"""
Restore Post 1111 from a specific Elementor revision.
Revision 1248 (2 days ago) = last good version BEFORE our wipe today.
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

# Get nonce from Post 1111 Elementor editor
el_url = 'https://brainyogaacademy.com/wp-admin/post.php?post=1111&action=elementor'
req = urllib.request.Request(el_url, headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    ed_html = resp.read().decode('utf-8')

ajax_nonce = re.search(r'\"ajax\":\{[^}]*\"nonce\":\"([^\"]+)\"', ed_html).group(1)
print(f"Nonce: {ajax_nonce}")

# Revision IDs from earlier check:
# 1290 = 5 min ago (our wipe save #2)
# 1289 = 5 min ago (our wipe save #1)  ← this was the bad one
# 1248 = 2 days ago ← GOOD ONE (before our changes today)
# We want to restore 1248!

# Try multiple revisions and find one with actual content
revision_ids = [1248]  # 2 days ago = good version

# Also check all revision IDs from the list
all_rev_ids = [1290, 1289, 1248]
print(f"\nChecking revisions: {all_rev_ids}")

for rev_id in all_rev_ids:
    actions_get = {
        'get_revision_data': {
            'action': 'get_revision_data',
            'data': {'id': str(rev_id), 'post_id': '1111'}
        }
    }
    ajax_data = urllib.parse.urlencode({
        'action': 'elementor_ajax',
        '_nonce': ajax_nonce,
        'editor_post_id': '1111',
        'actions': json.dumps(actions_get)
    }).encode()
    
    req2 = urllib.request.Request(
        'https://brainyogaacademy.com/wp-admin/admin-ajax.php',
        data=ajax_data,
        headers={'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/x-www-form-urlencoded'}
    )
    with opener.open(req2) as r:
        raw = r.read().decode('utf-8')
    
    try:
        resp_json = json.loads(raw)
        rev_data = resp_json.get('data', {}).get('responses', {}).get('get_revision_data', {})
        elements = rev_data.get('data', {}).get('elements', []) if rev_data.get('success') else []
        print(f"  Revision {rev_id}: {len(elements)} elements, success={rev_data.get('success')}")
        if elements and len(elements) > 2:
            print(f"  → FOUND GOOD REVISION: {rev_id} with {len(elements)} elements!")
            # Save elements
            with open(f'/tmp/rev_{rev_id}_elements.json', 'w') as f:
                json.dump(elements, f)
            print(f"    Saved to /tmp/rev_{rev_id}_elements.json")
    except Exception as e:
        print(f"  Revision {rev_id} error: {e}")
        print(f"  Raw (first 300): {raw[:300]}")
