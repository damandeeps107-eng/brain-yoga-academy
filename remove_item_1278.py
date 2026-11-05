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

# 1. Fetch nav-menus.php to get all inputs
req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/nav-menus.php?menu=5', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    html = resp.read().decode('utf-8')

# Search for delete link of 1278
delete_m = re.search(r'href=[\'"]([^\'"]*delete-menu-item=1278[^\'"]*)[\'"]', html)
if delete_m:
    del_url = delete_m.group(1).replace('&amp;', '&')
    if not del_url.startswith('http'):
        del_url = 'https://brainyogaacademy.com/wp-admin/' + del_url
    print("Deleting Item 1278 via:", del_url)
    req = urllib.request.Request(del_url, headers={'User-Agent': 'Mozilla/5.0'})
    with opener.open(req) as resp:
        print("Delete response status:", resp.status)
else:
    print("Delete link not found directly, removing from form submission...")
    form_m = re.search(r'<form[^>]*id=\"update-nav-menu\"[^>]*>(.*?)</form>', html, re.DOTALL)
    form_content = form_m.group(1)
    raw_inputs = re.findall(r'<input[^>]*name=[\'"]([^\'"]+)[\'"][^>]*value=[\'"]([^\'"]*)[\'"]', form_content)
    form_data = []
    for name, val in raw_inputs:
        if '1278' not in name:
            form_data.append((name, val))
    form_data.append(('save_menu', 'Save Menu'))
    encoded = urllib.parse.urlencode(form_data).encode('utf-8')
    req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/nav-menus.php', data=encoded, headers={'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/x-www-form-urlencoded'})
    with opener.open(req) as resp:
        print("Menu saved without 1278, status:", resp.status)

# Check Menu 5 now
req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/nav-menus.php?menu=5', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    res = resp.read().decode('utf-8')
    db_ids = re.findall(r'name=\"menu-item-db-id\[(\d+)\]\"', res)
    print("Menu 5 IDs now:", db_ids)
