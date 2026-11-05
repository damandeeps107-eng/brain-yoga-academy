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

# Check post 76 elementor data
req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/post.php?post=76&action=elementor', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    html = resp.read().decode('utf-8')

# Find elementor data in post 76
data_m = re.search(r'\"elements\":(\[.*?\]),\"controls\":', html)
if data_m:
    # Bracket balancer
    raw = html[data_m.start(1):]
    count = 0
    end_idx = 0
    for idx, ch in enumerate(raw):
        if ch == '[': count += 1
        elif ch == ']':
            count -= 1
            if count == 0:
                end_idx = idx + 1
                break
    elements = json.loads(raw[:end_idx])
    
    # Print all settings of all elements in Header 76
    def dump_el(el, depth=0):
        indent = '  ' * depth
        elType = el.get('elType')
        widgetType = el.get('widgetType')
        cid = el.get('id')
        st = el.get('settings', {})
        print(f"{indent}[{elType}:{widgetType or 'con'} id={cid}] settings={st}")
        for c in el.get('elements', []):
            dump_el(c, depth+1)
            
    for el in elements:
        dump_el(el)
