import urllib.request, urllib.parse, http.cookiejar, ssl

ctx = ssl._create_unverified_context()
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), urllib.request.HTTPSHandler(context=ctx))

login_url = 'https://brainyogaacademy.com/wp-login.php'
login_data = urllib.parse.urlencode({
    'log': 'rajendraboddu@gmail.com',
    'pwd': 'Gemini#1979',
    'wp-submit': 'Log In',
    'redirect_to': 'https://brainyogaacademy.com/wp-admin/',
    'testcookie': '1'
}).encode('utf-8')
opener.open(urllib.request.Request(login_url, data=login_data, headers={'User-Agent': 'Mozilla/5.0'}))

# Purge All
purge_url = 'https://brainyogaacademy.com/wp-admin/index.php?LSCWP_CTRL=purge&LSCWP_NONCE=663a0c4afd&litespeed_type=purge_all'
req = urllib.request.Request(purge_url, headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    print("Purge all response code:", resp.status)

# Also re-save Header 76 in Elementor so Elementor's internal HTML cache of Header 76 updates
el_url = 'https://brainyogaacademy.com/wp-admin/post.php?post=76&action=elementor'
req = urllib.request.Request(el_url, headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    html = resp.read().decode('utf-8')

import re, json
ajax_nonce = re.search(r'\"ajax\":\{[^}]*\"nonce\":\"([^\"]+)\"', html).group(1)
print("Got Elementor nonce for post 76:", ajax_nonce)

# Call Elementor tools clear cache
clear_cache_data = urllib.parse.urlencode({
    'action': 'elementor_clear_cache',
    '_nonce': ajax_nonce
}).encode('utf-8')
try:
    req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/admin-ajax.php', data=clear_cache_data, headers={'User-Agent': 'Mozilla/5.0'})
    with opener.open(req) as resp:
        print("Elementor clear cache response:", resp.read().decode('utf-8')[:200])
except Exception as e:
    print("Elementor clear cache error:", e)
