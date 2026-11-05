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

# Open Elementor editor for Post 76
req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/post.php?post=76&action=elementor', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    html = resp.read().decode('utf-8')

# Search for elementor elements in Post 76
elements_m = re.search(r'\"elements\":(\[.*?\]),\"controls\":', html)
if elements_m:
    elements = json.loads(elements_m.group(1))
    print(f"Template 76 has {len(elements)} root elements!")
    
    # Check widgets inside
    def inspect_w(el):
        wt = el.get('widgetType')
        st = el.get('settings', {})
        if wt:
            print(f"Widget: {wt} | Settings: {list(st.keys())}")
            if 'menu' in st:
                print(f"  --> Nav Menu Selected: {st.get('menu')}")
            if 'text' in st:
                print(f"  --> Button Text: {st.get('text')}")
        for c in el.get('elements', []):
            inspect_w(c)
    for el in elements:
        inspect_w(el)
else:
    print("Could not find elements json in post 76")
