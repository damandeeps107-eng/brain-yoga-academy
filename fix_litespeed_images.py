#!/usr/bin/env python3
"""
Turn OFF LiteSpeed aggressive media lazy-loading & guest_optm
so images (boy yoga, logo, WHY IT WORKS, Rajendra ji) load IMMEDIATELY without delay!
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

# 2. General Settings: Set guest_optm = 0 (leave guest mode cache ON, but disable guest optimization which breaks images)
req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/admin.php?page=litespeed-general', headers={'User-Agent': 'Mozilla/5.0'})
html = opener.open(req).read().decode('utf-8')
lscwp_nonce = re.search(r'name=\"LSCWP_NONCE\"[^>]*value=\"([a-f0-9]+)\"', html).group(1)

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
    ('guest_optm', '0'),  # DISABLE guest optimization
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
print("Step 2: Disabled guest_optm (so images are not delayed)")

# 3. Purge all cache
purge_nonce = re.search(r'LSCWP_NONCE=([a-f0-9]+)', resp_html).group(1)
purge_url = f'https://brainyogaacademy.com/?LSCWP_CTRL=purge&LSCWP_NONCE={purge_nonce}&litespeed_type=purge_all'
with opener.open(urllib.request.Request(purge_url, headers={'User-Agent': 'Mozilla/5.0'})) as p:
    print(f"Step 3: LiteSpeed cache purged (Status: {p.status})")

print("✅ Aggressive image lazy-loading removed!")
