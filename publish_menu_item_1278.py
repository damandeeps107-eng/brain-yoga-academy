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

# Fetch nav-menus.php
req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/nav-menus.php?menu=5', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    html = resp.read().decode('utf-8')

# Search for the form
form_m = re.search(r'<form[^>]*id=\"update-nav-menu\"[^>]*>(.*?)</form>', html, re.DOTALL)
form_content = form_m.group(1)

# Extract all input fields
raw_inputs = re.findall(r'<input[^>]*name=[\'"]([^\'"]+)[\'"][^>]*value=[\'"]([^\'"]*)[\'"]', form_content)
form_data = []
for name, val in raw_inputs:
    if name == 'menu-item-status[1278]':
        form_data.append((name, 'publish'))
    else:
        form_data.append((name, val))

# Ensure menu-item-status[1278] is publish
if not any(k == 'menu-item-status[1278]' for k, v in form_data):
    form_data.append(('menu-item-status[1278]', 'publish'))

form_data.append(('save_menu', 'Save Menu'))

encoded_data = urllib.parse.urlencode(form_data).encode('utf-8')
save_req = urllib.request.Request(
    'https://brainyogaacademy.com/wp-admin/nav-menus.php',
    data=encoded_data,
    headers={'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/x-www-form-urlencoded'}
)

with opener.open(save_req) as resp:
    res_html = resp.read().decode('utf-8')
    print("Save menu status:", resp.status)
    m = re.findall(r'<li[^>]*id=\"menu-item-1278\"[^>]*>.*?</li>', res_html, re.DOTALL)
    if m:
        print("Item 1278 after save:")
        print(m[0][:400])
        print("Is still pending:", 'pending' in m[0])
