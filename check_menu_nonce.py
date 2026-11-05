import urllib.request, urllib.parse, http.cookiejar, ssl, re

ctx = ssl._create_unverified_context()
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), urllib.request.HTTPSHandler(context=ctx))

# Login
login_url = 'https://brainyogaacademy.com/wp-login.php'
login_data = urllib.parse.urlencode({
    'log': 'rajendraboddu@gmail.com',
    'pwd': 'Gemini#1979',
    'wp-submit': 'Log In',
    'redirect_to': 'https://brainyogaacademy.com/wp-admin/',
    'testcookie': '1'
}).encode('utf-8')
opener.open(urllib.request.Request(login_url, data=login_data, headers={'User-Agent': 'Mozilla/5.0'}))

# Inspect nav-menus.php
req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/nav-menus.php?menu=5', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    html = resp.read().decode('utf-8')

# Search for menu-settings-column-nonce
nonce_m = re.search(r'id=\"menu-settings-column-nonce\" name=\"menu-settings-column-nonce\" value=\"([^\"]+)\"', html)
if nonce_m:
    print("Found menu-settings-column-nonce:", nonce_m.group(1))

# Search for update-nav_menu nonce
update_nonce_m = re.search(r'id=\"_wpnonce\" name=\"_wpnonce\" value=\"([^\"]+)\"', html)
if update_nonce_m:
    print("Found update-nav_menu nonce:", update_nonce_m.group(1))
