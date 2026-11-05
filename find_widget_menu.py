import urllib.request, urllib.parse, http.cookiejar, ssl, re, json

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

# Inspect post.php?post=76&action=elementor
req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/post.php?post=76&action=elementor', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    html = resp.read().decode('utf-8')

# Search for 0d80f0c settings
m = re.search(r'\"id\":\"0d80f0c\"[^\}]*\"settings\":\{([^\}]+)\}', html)
if m:
    print("Widget 0d80f0c settings:", m.group(1))

m2 = re.search(r'\"id\":\"a846a79\"[^\}]*\"settings\":\{([^\}]+)\}', html)
if m2:
    print("Widget a846a79 settings:", m2.group(1))
