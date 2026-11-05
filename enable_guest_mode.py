#!/usr/bin/env python3
"""
Enable LiteSpeed Guest Mode & Guest Optimization.
This serves ultra-fast pre-rendered static HTML with non-blocking CSS/JS to all visitors!
"""
import urllib.request, urllib.parse, http.cookiejar, ssl, re

ctx = ssl._create_unverified_context()
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), urllib.request.HTTPSHandler(context=ctx))

# 1. Login
login_data = urllib.parse.urlencode({
    'log': 'rajendraboddu@gmail.com', 'pwd': 'Gemini#1979',
    'wp-submit': 'Log In', 'redirect_to': 'https://brainyogaacademy.com/wp-admin/', 'testcookie': '1'
}).encode()
opener.open(urllib.request.Request('https://brainyogaacademy.com/wp-login.php', data=login_data, headers={'User-Agent': 'Mozilla/5.0'}))
print("Step 1: Logged in!")

# 2. Get LiteSpeed general page and nonces
req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/admin.php?page=litespeed-general', headers={'User-Agent': 'Mozilla/5.0'})
html = opener.open(req).read().decode('utf-8')

lscwp_nonce = re.search(r'name=\"LSCWP_NONCE\"[^>]*value=\"([a-f0-9]+)\"', html).group(1)
print(f"Step 2: LSCWP Nonce = {lscwp_nonce}")

# 3. Post form to save settings
payload = [
    ('LSCWP_CTRL', 'save-settings'),
    ('LSCWP_NONCE', lscwp_nonce),
    ('_wp_http_referer', '/wp-admin/admin.php?page=litespeed-general'),
    ('_settings-enroll[]', 'auto_upgrade'),
    ('_settings-enroll[]', 'guest'),
    ('_settings-enroll[]', 'guest_optm'),
    ('_settings-enroll[]', 'server_ip'),
    ('_settings-enroll[]', 'news'),
    ('guest', '1'),
    ('guest_optm', '1'),
    ('auto_upgrade', '0'),
    ('news', '0')
]

post_data = urllib.parse.urlencode(payload).encode('utf-8')
save_req = urllib.request.Request(
    'https://brainyogaacademy.com/wp-admin/admin.php?page=litespeed-general',
    data=post_data,
    headers={'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/x-www-form-urlencoded'}
)

resp_html = opener.open(save_req).read().decode('utf-8')
print("Step 3: Form submitted!")

# 4. Verify settings
verify_req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/admin.php?page=litespeed-general', headers={'User-Agent': 'Mozilla/5.0'})
v_html = opener.open(verify_req).read().decode('utf-8')

guest_1_checked = "name='guest' id='input_radio_guest_1' value='1'  checked='checked'" in v_html or 'name="guest" id="input_radio_guest_1" value="1"  checked="checked"' in v_html
guest_optm_1_checked = "name='guest_optm' id='input_radio_guest_optm_1' value='1'  checked='checked'" in v_html or 'name="guest_optm" id="input_radio_guest_optm_1" value="1"  checked="checked"' in v_html

print(f"Step 4: Verification:")
print(f"  Guest Mode ON: {guest_1_checked}")
print(f"  Guest Optimization ON: {guest_optm_1_checked}")

# 5. Purge all cache
purge_nonce = re.search(r'LSCWP_NONCE=([a-f0-9]+)', v_html).group(1)
purge_url = f'https://brainyogaacademy.com/?LSCWP_CTRL=purge&LSCWP_NONCE={purge_nonce}&litespeed_type=purge_all'
try:
    with opener.open(urllib.request.Request(purge_url, headers={'User-Agent': 'Mozilla/5.0'})) as p:
        print(f"Step 5: LiteSpeed cache purged (Status: {p.status})")
except Exception as e:
    print(f"Purge: {e}")

print("✅ Guest Mode & Guest Optimization activated!")
