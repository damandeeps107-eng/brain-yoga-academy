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

# Inspect nav-menus.php content
req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/nav-menus.php', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    html = resp.read().decode('utf-8')

# Current menu id
cur_menu = re.search(r'id=\"menu\"\s+value=\"(\d+)\"', html)
if cur_menu:
    print("Current active menu ID:", cur_menu.group(1))

# Find menu items in list
items = re.findall(r'<li[^>]*id=\"menu-item-(\d+)\"[^>]*>.*?<span class=\"menu-item-title\">([^<]+)</span>', html, re.DOTALL)
print("Current Menu Items in Menu:")
for mid, title in items:
    print(f"  - Item {mid}: {title.strip()}")
