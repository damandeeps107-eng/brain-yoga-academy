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

# 1. Fetch nav-menus.php to get fresh nonces
req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/nav-menus.php?menu=5', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    html = resp.read().decode('utf-8')

col_nonce = re.search(r'id=\"menu-settings-column-nonce\" name=\"menu-settings-column-nonce\" value=\"([^\"]+)\"', html).group(1)
print("Got column nonce:", col_nonce)

# 2. Add custom link via AJAX
add_data = urllib.parse.urlencode({
    'action': 'add-menu-item',
    'menu': '5',
    'menu-settings-column-nonce': col_nonce,
    'menu-item[-1][menu-item-type]': 'custom',
    'menu-item[-1][menu-item-title]': 'For Adults (Busy Minds)',
    'menu-item[-1][menu-item-url]': 'https://brainyogaacademy.com/brain-yoga-for-busy-minds/'
}).encode('utf-8')

ajax_req = urllib.request.Request(
    'https://brainyogaacademy.com/wp-admin/admin-ajax.php',
    data=add_data,
    headers={'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/x-www-form-urlencoded'}
)

with opener.open(ajax_req) as resp:
    res_html = resp.read().decode('utf-8')
    print("Add menu item response status:", resp.status)
    print("New item id matched:", re.findall(r'menu-item-(\d+)', res_html))

# 3. Now let's save the menu to persist it
# Fetch nav-menus.php again to get update nonce and all menu item IDs
req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/nav-menus.php?menu=5', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    menu_page = resp.read().decode('utf-8')

# Search for the form on nav-menus.php
form_m = re.search(r'<form[^>]*id=\"update-nav-menu\"[^>]*>(.*?)</form>', menu_page, re.DOTALL)
if form_m:
    form_content = form_m.group(1)
    # Extract all inputs
    inputs = re.findall(r'<input[^>]*name=[\'"]([^\'"]+)[\'"][^>]*value=[\'"]([^\'"]*)[\'"]', form_content)
    form_fields = {name: val for name, val in inputs}
    form_fields['save_menu'] = 'Save Menu'
    
    update_data = urllib.parse.urlencode(form_fields).encode('utf-8')
    post_req = urllib.request.Request(
        'https://brainyogaacademy.com/wp-admin/nav-menus.php',
        data=update_data,
        headers={'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/x-www-form-urlencoded'}
    )
    with opener.open(post_req) as resp:
        print("Menu updated successfully! Status:", resp.status)
