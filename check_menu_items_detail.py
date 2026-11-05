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

# Check nav-menus.php HTML form inputs
req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/nav-menus.php?menu=5', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    html = resp.read().decode('utf-8')

# Find all menu-item-db-id in the HTML
db_ids = re.findall(r'name=\"menu-item-db-id\[(\d+)\]\"', html)
print("Found menu-item-db-ids currently in Menu 5:", db_ids)

for db_id in db_ids:
    title_m = re.search(rf'id=\"edit-menu-item-title-{db_id}\"[^>]*value=\"([^\"]*)\"', html)
    url_m = re.search(rf'id=\"edit-menu-item-url-{db_id}\"[^>]*value=\"([^\"]*)\"', html)
    t = title_m.group(1) if title_m else 'Unknown'
    u = url_m.group(1) if url_m else 'Unknown'
    print(f"  Item {db_id}: Title='{t}' | URL='{u}'")
