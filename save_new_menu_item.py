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

form_m = re.search(r'<form[^>]*id=\"update-nav-menu\"[^>]*>(.*?)</form>', html, re.DOTALL)
form_content = form_m.group(1)

# Extract all input fields from the form
raw_inputs = re.findall(r'<input[^>]*name=[\'"]([^\'"]+)[\'"][^>]*value=[\'"]([^\'"]*)[\'"]', form_content)
form_data = []
for name, val in raw_inputs:
    form_data.append((name, val))

# Add new menu item (Item 0)
new_item_fields = [
    ('menu-item-db-id[0]', '0'),
    ('menu-item-object-id[0]', '1242'),
    ('menu-item-object[0]', 'page'),
    ('menu-item-parent-id[0]', '0'),
    ('menu-item-position[0]', '5'),
    ('menu-item-type[0]', 'post_type'),
    ('menu-item-title[0]', 'For Adults (Busy Minds)'),
    ('menu-item-url[0]', 'https://brainyogaacademy.com/brain-yoga-for-busy-minds/'),
    ('menu-item-description[0]', ''),
    ('menu-item-attr-title[0]', ''),
    ('menu-item-target[0]', ''),
    ('menu-item-classes[0]', ''),
    ('menu-item-xfn[0]', '')
]

for k, v in new_item_fields:
    form_data.append((k, v))

form_data.append(('save_menu', 'Save Menu'))

encoded_data = urllib.parse.urlencode(form_data).encode('utf-8')
save_req = urllib.request.Request(
    'https://brainyogaacademy.com/wp-admin/nav-menus.php',
    data=encoded_data,
    headers={'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/x-www-form-urlencoded'}
)

with opener.open(save_req) as resp:
    res_html = resp.read().decode('utf-8')
    print("Save menu response code:", resp.status)
    db_ids_after = re.findall(r'name=\"menu-item-db-id\[(\d+)\]\"', res_html)
    print("Menu-item-db-ids after saving:", db_ids_after)
