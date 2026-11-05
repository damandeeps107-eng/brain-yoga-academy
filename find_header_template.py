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

# Check Saved Templates in Elementor
req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/edit.php?post_type=elementor_library', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    html = resp.read().decode('utf-8')

templates = re.findall(r'<tr[^>]*id=\"post-(\d+)\"[^>]*>.*?<a class=\"row-title\"[^>]*>([^<]+)</a>', html, re.DOTALL)
print("Elementor Library Templates found:")
for tid, title in templates:
    print(f"  - Template {tid}: {title.strip()}")

# Also check Theme Builder
req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/admin.php?page=elementor-app', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    tb_html = resp.read().decode('utf-8')
    print("Elementor App page status 200 OK, length:", len(tb_html))
