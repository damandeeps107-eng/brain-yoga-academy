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

# Open Elementor editor for Post 76
req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/post.php?post=76&action=elementor', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    html = resp.read().decode('utf-8')

# Search for widgetTypes and menus
widgets = re.findall(r'\"widgetType\":\"([^\"]+)\"', html)
print("Widgets in Header 76:", widgets)

# Search for buttons and nav menus
buttons = re.findall(r'\"widgetType\":\"button\"[^\}]*\"text\":\"([^\"]+)\"', html)
print("Buttons in Header 76:", buttons)

menus = re.findall(r'\"widgetType\":\"nav-menu\"[^\}]*\"menu\":\"([^\"]+)\"', html)
print("Nav menus in Header 76:", menus)

# Search for any links
links = re.findall(r'\"url\":\"(https?://[^\"]+)\"', html)
print("Links in Header 76:", links)
