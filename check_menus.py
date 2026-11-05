import urllib.request, urllib.parse, http.cookiejar, ssl, json, re

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
req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/nav-menus.php', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    html = resp.read().decode('utf-8')

print("Nav menus page title:", re.findall(r'<title>(.*?)</title>', html))
menus = re.findall(r'<select[^>]*name=[\'"]menu[\'"][^>]*>(.*?)</select>', html, re.DOTALL)
if menus:
    print("Available menus in select:", re.findall(r'<option[^>]*value=[\'"]([^\'"]*)[\'"][^>]*>(.*?)</option>', menus[0]))

# Check menu locations
locations = re.findall(r'menu-locations\[([^\]]+)\]', html)
print("Menu locations found:", locations)
