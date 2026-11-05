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

# Check nav-menus.php?action=locations
req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/nav-menus.php?action=locations', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    html = resp.read().decode('utf-8')

# Find primary menu selection
locs = re.findall(r'<select[^>]*name=[\'"]menu-locations\[primary\][\'"][^>]*>(.*?)</select>', html, re.DOTALL)
if locs:
    print("Primary location dropdown:")
    print(locs[0])
else:
    print("No primary select found. Checking all select elements in locations page:")
    selects = re.findall(r'<select[^>]*name=[\'"]([^\'"]+)[\'"][^>]*>(.*?)</select>', html, re.DOTALL)
    for name, content in selects:
        print(f"Select: {name}")
        selected = re.findall(r'<option[^>]*value=[\'"]([^\'"]*)[\'"][^>]*selected[^>]*>(.*?)</option>', content)
        print("  Selected:", selected)
