import urllib.request, urllib.parse, http.cookiejar, ssl, re

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

# Check active plugins
req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/plugins.php', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    html = resp.read().decode('utf-8')

# Search for active plugins
active_plugins = re.findall(r'<tr[^>]*class=[\'"][^\'"]*active[^\'"]*[\'"][^>]*data-plugin=[\'"]([^\'"]+)[\'"]', html)
print("Active Plugins:", active_plugins)

# Check Item 1278 in nav-menus.php
req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/nav-menus.php?menu=5', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    menu_html = resp.read().decode('utf-8')

print("Is 1278 in Menu 5:", '1278' in menu_html)
title_m = re.search(r'id=\"edit-menu-item-title-1278\"[^>]*value=\"([^\"]*)\"', menu_html)
if title_m:
    print("Item 1278 Title:", title_m.group(1))
url_m = re.search(r'id=\"edit-menu-item-url-1278\"[^>]*value=\"([^\"]*)\"', menu_html)
if url_m:
    print("Item 1278 URL:", url_m.group(1))
