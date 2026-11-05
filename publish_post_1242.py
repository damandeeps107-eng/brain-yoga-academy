import urllib.request, urllib.parse, http.cookiejar, ssl, json, re

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

# Open Elementor editor for Post 1242 to get fresh ajax nonce
el_url = 'https://brainyogaacademy.com/wp-admin/post.php?post=1242&action=elementor'
req = urllib.request.Request(el_url, headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    html = resp.read().decode('utf-8')

ajax_nonce = re.search(r'\"ajax\":\{[^}]*\"nonce\":\"([^\"]+)\"', html).group(1)
print('Got Elementor ajax nonce:', ajax_nonce)

# Load native template elements
with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain_yoga_elementor_native_template.json', 'r') as f:
    template_data = json.load(f)

elements = template_data['content']
print(f'Publishing {len(elements)} containers to Post 1242...')

# Call save_builder with status: publish
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
    'editor_post_id': '1242',
    'actions': json.dumps(actions)
}).encode('utf-8')

ajax_req = urllib.request.Request(
    'https://brainyogaacademy.com/wp-admin/admin-ajax.php',
    data=ajax_data,
    headers={
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
)

with opener.open(ajax_req) as resp:
    res = json.loads(resp.read().decode('utf-8'))
    save_result = res.get('data', {}).get('responses', {}).get('save_builder', {})
    if save_result.get('success'):
        print('SUCCESS! Post 1242 is now officially PUBLISHED and LIVE!')
        print('Live Status:', save_result.get('data', {}).get('status'))
        print('Public URL: https://brainyogaacademy.com/brain-yoga-for-busy-minds/')
    else:
        print('Publish failed:', res)
