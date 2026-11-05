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

# Check post.php?post=1242&action=edit
req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/post.php?post=1242&action=edit', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    html = resp.read().decode('utf-8')

# Find page_template select
tmpl_m = re.findall(r'<select[^>]*name=[\'"]page_template[\'"][^>]*>(.*?)</select>', html, re.DOTALL)
if tmpl_m:
    print("Page template options:")
    print(tmpl_m[0])
    selected = re.findall(r'<option[^>]*value=[\'"]([^\'"]*)[\'"][^>]*selected[^>]*>(.*?)</option>', tmpl_m[0])
    print("Currently selected template:", selected)
