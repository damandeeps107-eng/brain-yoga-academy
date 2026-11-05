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

# 1. Open post.php?post=76&action=elementor to get elements and nonce
el_url = 'https://brainyogaacademy.com/wp-admin/post.php?post=76&action=elementor'
req = urllib.request.Request(el_url, headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    html = resp.read().decode('utf-8')

ajax_nonce = re.search(r'\"ajax\":\{[^}]*\"nonce\":\"([^\"]+)\"', html).group(1)
print("Got Elementor nonce:", ajax_nonce)

# Extract elementor data config from page
config_m = re.search(r'elementorFrontendConfig\s*=\s*(\{.*?\});\s*<\/script>', html, re.DOTALL)
# Or search for elements in initial document
init_m = re.search(r'\"elements\":(\[.*?\]),\"controls\":', html)
if init_m:
    # Bracket balancer to extract full JSON
    raw = html[init_m.start(1):]
    count = 0
    end_idx = 0
    for idx, ch in enumerate(raw):
        if ch == '[': count += 1
        elif ch == ']':
            count -= 1
            if count == 0:
                end_idx = idx + 1
                break
    elements_json = raw[:end_idx]
    elements = json.loads(elements_json)
    print(f"Loaded {len(elements)} root elements from Header 76!")

    # Call save_builder to recompile Header 76
    actions = {
        'save_builder': {
            'action': 'save_builder',
            'data': {
                'status': 'publish',
                'elements': elements
            }
        }
    }
    ajax_data = urllib.parse.urlencode({
        'action': 'elementor_ajax',
        '_nonce': ajax_nonce,
        'editor_post_id': '76',
        'actions': json.dumps(actions)
    }).encode('utf-8')
    ajax_req = urllib.request.Request(
        'https://brainyogaacademy.com/wp-admin/admin-ajax.php',
        data=ajax_data,
        headers={'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/x-www-form-urlencoded'}
    )
    with opener.open(ajax_req) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        save_res = res.get('data', {}).get('responses', {}).get('save_builder', {})
        print("Save builder Header 76 success:", save_res.get('success'))
