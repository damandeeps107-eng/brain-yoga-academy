#!/usr/bin/env python3
"""
Enable LiteSpeed Page Optimizations:
- CSS Minify
- JS Minify
- JS Defer (huge for perceived page load speed!)
- HTML Minify
- DNS Prefetch
- Emoji Removal
- Query String Removal
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
print("Logged in!")

# 2. Get LiteSpeed page optm form and current nonces
req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/admin.php?page=litespeed-page_optm', headers={'User-Agent': 'Mozilla/5.0'})
html = opener.open(req).read().decode('utf-8')

lscwp_nonce = re.search(r'name=\"LSCWP_NONCE\"[^>]*value=\"([a-f0-9]+)\"', html).group(1)
print(f"LSCWP Nonce: {lscwp_nonce}")

# 3. Submit optimized settings
form_payload = [
    ('LSCWP_CTRL', 'save-settings'),
    ('LSCWP_NONCE', lscwp_nonce),
    ('_wp_http_referer', '/wp-admin/admin.php?page=litespeed-page_optm'),
    ('optm-css_min', '1'),
    ('optm-js_min', '1'),
    ('optm-js_defer', '1'),
    ('optm-html_min', '1'),
    ('optm-dns_prefetch_ctrl', '1'),
    ('optm-emoji_rm', '1'),
    ('optm-qs_rm', '1'),
    ('optm-ggfonts_rm', '0'),
]

post_data = urllib.parse.urlencode(form_payload).encode('utf-8')
save_req = urllib.request.Request(
    'https://brainyogaacademy.com/wp-admin/admin.php?page=litespeed-page_optm',
    data=post_data,
    headers={'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/x-www-form-urlencoded'}
)

resp = opener.open(save_req).read().decode('utf-8')
print("Settings submitted!")

# Verify if settings got saved
check_req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/admin.php?page=litespeed-page_optm', headers={'User-Agent': 'Mozilla/5.0'})
check_html = opener.open(check_req).read().decode('utf-8')

css_min_checked = 'name="optm-css_min" value="1" checked' in check_html
js_min_checked = 'name="optm-js_min" value="1" checked' in check_html
js_defer_checked = 'name="optm-js_defer" value="1" checked' in check_html

print(f"Verified settings:")
print(f"  CSS Minify enabled: {css_min_checked}")
print(f"  JS Minify enabled: {js_min_checked}")
print(f"  JS Defer enabled: {js_defer_checked}")

# Purge cache
purge_nonce = re.search(r'LSCWP_NONCE=([a-f0-9]+)', check_html).group(1)
purge_url = f'https://brainyogaacademy.com/?LSCWP_CTRL=purge&LSCWP_NONCE={purge_nonce}&litespeed_type=purge_all'
try:
    with opener.open(urllib.request.Request(purge_url, headers={'User-Agent': 'Mozilla/5.0'})) as p:
        print(f"Cache purged: {p.status}")
except Exception as e:
    print(f"Purge note: {e}")
