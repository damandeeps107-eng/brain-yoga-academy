import urllib.request, urllib.parse, http.cookiejar, ssl, re, json

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

# Check all menus in WP
req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/nav-menus.php', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    html = resp.read().decode('utf-8')

# Find all menu dropdown options
menu_options = re.findall(r'<select[^>]*name=[\'"]menu[\'"][^>]*>(.*?)</select>', html, re.DOTALL)
if menu_options:
    opts = re.findall(r'<option[^>]*value=[\'"]([^\'"]*)[\'"][^>]*>(.*?)</option>', menu_options[0])
    print("All Menus in WordPress:")
    for val, name in opts:
        print(f"  - Menu ID {val}: {name.strip()}")

# Check all Elementor Header & Footer templates if any
req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/edit.php?post_type=elementor-hf', headers={'User-Agent': 'Mozilla/5.0'})
try:
    with opener.open(req) as resp:
        hf_html = resp.read().decode('utf-8')
        print("Elementor HF templates:", re.findall(r'<tr[^>]*id=\"post-(\d+)\"', hf_html))
except Exception as e:
    print("No elementor-hf post type:", e)

# Check Post 1111 Elementor data
req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/post.php?post=1111&action=elementor', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    el_html = resp.read().decode('utf-8')
    # search for nav-menu widget settings in post 1111
    nav_widgets = re.findall(r'\"widgetType\":\"nav-menu\"[^\}]*\}', el_html)
    print("Post 1111 has nav-menu widgets:", len(nav_widgets))
    menu_ids = re.findall(r'\"menu\":\"([^\"]+)\"', el_html)
    print("Menu IDs referenced in Post 1111:", set(menu_ids))
