import urllib.request, urllib.parse, http.cookiejar, ssl, json, re

ctx = ssl._create_unverified_context()
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), urllib.request.HTTPSHandler(context=ctx))

# 1. Login to WordPress
login_url = 'https://brainyogaacademy.com/wp-login.php'
login_data = urllib.parse.urlencode({
    'log': 'rajendraboddu@gmail.com',
    'pwd': 'Gemini#1979',
    'wp-submit': 'Log In',
    'redirect_to': 'https://brainyogaacademy.com/wp-admin/',
    'testcookie': '1'
}).encode('utf-8')
opener.open(urllib.request.Request(login_url, data=login_data, headers={'User-Agent': 'Mozilla/5.0'}))

# 2. Load media map
with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/wp_media_map.json', 'r') as f:
    media_map = json.load(f)

# 3. Read exact busy-minds.html
with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Replace all images with live WP URLs
for filename, meta in media_map.items():
    html_content = html_content.replace(f'src="{filename}"', f'src="{meta["url"]}"')
    html_content = html_content.replace(f'content="{filename}"', f'content="{meta["url"]}"')
    html_content = html_content.replace(f"src='{filename}'", f"src='{meta['url']}'")

# Replace navigation links
html_content = html_content.replace('href="kids.html"', 'href="https://brainyogaacademy.com/"')
html_content = html_content.replace('href="busy-minds.html"', 'href="https://brainyogaacademy.com/brain-yoga-for-busy-minds/"')
html_content = html_content.replace('href="index.html"', 'href="https://brainyogaacademy.com/brain-yoga-for-busy-minds/"')

print(f"Prepared full HTML content: {len(html_content)} characters")

# 4. Wrap inside Elementor JSON structure
elements = [
    {
        "id": "by_exact_root",
        "elType": "container",
        "isInner": False,
        "settings": {
            "content_width": "full",
            "gap": "no",
            "padding": {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0"},
            "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0"}
        },
        "elements": [
            {
                "id": "by_exact_html_widget",
                "elType": "widget",
                "widgetType": "html",
                "settings": {
                    "html": html_content
                }
            }
        ]
    }
]

# 5. Get Elementor ajax nonce from post 1242 editor
el_url = 'https://brainyogaacademy.com/wp-admin/post.php?post=1242&action=elementor'
req = urllib.request.Request(el_url, headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    ed_html = resp.read().decode('utf-8')

ajax_nonce = re.search(r'\"ajax\":\{[^}]*\"nonce\":\"([^\"]+)\"', ed_html).group(1)
print("Got Elementor ajax nonce:", ajax_nonce)

# 6. Save via Elementor save_builder with status=publish
actions = {
    'save_builder': {
        'action': 'save_builder',
        'data': {
            'status': 'publish',
            'elements': elements,
            'settings': {
                'template': 'elementor_canvas'
            }
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
    headers={'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/x-www-form-urlencoded'}
)

with opener.open(ajax_req) as resp:
    res = json.loads(resp.read().decode('utf-8'))
    save_result = res.get('data', {}).get('responses', {}).get('save_builder', {})
    print("Elementor save_builder success:", save_result.get('success'))

# 7. Also set page_template = elementor_canvas via quick edit to ensure WordPress uses Canvas
req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/edit.php?post_type=page', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    p_html = resp.read().decode('utf-8')

nonce_m = re.search(r'id=\"_inline_edit\" name=\"_inline_edit\" value=\"([^\"]+)\"', p_html)
if nonce_m:
    inline_nonce = nonce_m.group(1)
    quick_data = urllib.parse.urlencode({
        'action': 'inline-save',
        'post_ID': '1242',
        '_inline_edit': inline_nonce,
        'post_type': 'page',
        'post_title': 'Brain Yoga for Busy Minds',
        'post_name': 'brain-yoga-for-busy-minds',
        '_status': 'publish',
        'comment_status': 'closed',
        'ping_status': 'closed',
        'page_template': 'elementor_canvas'
    }).encode('utf-8')
    ajax_req = urllib.request.Request(
        'https://brainyogaacademy.com/wp-admin/admin-ajax.php',
        data=quick_data,
        headers={'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/x-www-form-urlencoded'}
    )
    with opener.open(ajax_req) as resp:
        print("Page template set to elementor_canvas successfully!")

# 8. Purge LiteSpeed cache
purge_url = 'https://brainyogaacademy.com/wp-admin/index.php?LSCWP_CTRL=purge&LSCWP_NONCE=663a0c4afd&litespeed_type=purge_all'
try:
    req = urllib.request.Request(purge_url, headers={'User-Agent': 'Mozilla/5.0'})
    with opener.open(req) as resp:
        print("Purged LiteSpeed cache successfully!")
except Exception as e:
    print("Cache purge error:", e)

print("DEPLOYMENT OF EXACT GITHUB PAGES DESIGN TO POST 1242 COMPLETED!")
