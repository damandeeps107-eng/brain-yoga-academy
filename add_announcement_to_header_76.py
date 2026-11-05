import urllib.request, urllib.parse, http.cookiejar, ssl, json, re

ctx = ssl._create_unverified_context()
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), urllib.request.HTTPSHandler(context=ctx))

# 1. Login to WP
login_url = 'https://brainyogaacademy.com/wp-login.php'
login_data = urllib.parse.urlencode({
    'log': 'rajendraboddu@gmail.com',
    'pwd': 'Gemini#1979',
    'wp-submit': 'Log In',
    'redirect_to': 'https://brainyogaacademy.com/wp-admin/',
    'testcookie': '1'
}).encode('utf-8')
opener.open(urllib.request.Request(login_url, data=login_data, headers={'User-Agent': 'Mozilla/5.0'}))

# 2. Get Header 76 current elements
with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/header_76_elements.json', 'r') as f:
    elements = json.load(f)

# Filter out any existing by_top_announcement_bar
clean_elements = [el for el in elements if el.get('id') != 'by_top_announcement_bar']

# Create the top announcement bar container
announcement_bar = {
    "id": "by_top_announcement_bar",
    "elType": "container",
    "isInner": False,
    "settings": {
        "content_width": "full",
        "background_background": "classic",
        "background_color": "#007984",
        "padding": {
            "unit": "px",
            "top": "8",
            "right": "16",
            "bottom": "8",
            "left": "16",
            "isLinked": False
        },
        "z_index": 9999
    },
    "elements": [
        {
            "id": "by_top_announcement_html",
            "elType": "widget",
            "widgetType": "html",
            "settings": {
                "html": """<div style="display:flex;align-items:center;justify-content:center;gap:8px;flex-wrap:wrap;text-align:center;font-family:'Poppins',-apple-system,BlinkMacSystemFont,sans-serif;font-size:12px;color:#FFFFFF;line-height:1.4;">
    <span style="display:inline-block;padding:2px 10px;border-radius:9999px;font-size:10px;font-weight:700;text-transform:uppercase;background-color:#FD8742;color:#FFFFFF;letter-spacing:0.05em;white-space:nowrap;">
        Adult Wellness
    </span>
    <span style="font-weight:500;">Looking for stress relief, focus & brain yoga for working professionals?</span>
    <a href="https://brainyogaacademy.com/brain-yoga-for-busy-minds/" style="display:inline-flex;align-items:center;gap:4px;font-weight:700;color:#FFE8DA;text-decoration:underline;white-space:nowrap;">
        <span>Visit Brain Yoga For Busy Minds &rarr;</span>
    </a>
</div>"""
            }
        }
    ]
}

new_elements = [announcement_bar] + clean_elements

# 3. Get Elementor nonce for post 76
el_url = 'https://brainyogaacademy.com/wp-admin/post.php?post=76&action=elementor'
req = urllib.request.Request(el_url, headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    ed_html = resp.read().decode('utf-8')

ajax_nonce = re.search(r'\"ajax\":\{[^}]*\"nonce\":\"([^\"]+)\"', ed_html).group(1)
print("Got Elementor ajax nonce for Header 76:", ajax_nonce)

# 4. Save via save_builder
actions = {
    'save_builder': {
        'action': 'save_builder',
        'data': {
            'status': 'publish',
            'elements': new_elements
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
    save_result = res.get('data', {}).get('responses', {}).get('save_builder', {})
    print("Elementor save_builder Header 76 success:", save_result.get('success'))

# 5. Purge LiteSpeed cache
purge_url = 'https://brainyogaacademy.com/wp-admin/index.php?LSCWP_CTRL=purge&LSCWP_NONCE=663a0c4afd&litespeed_type=purge_all'
try:
    req = urllib.request.Request(purge_url, headers={'User-Agent': 'Mozilla/5.0'})
    with opener.open(req) as resp:
        print("Purged LiteSpeed cache successfully!")
except Exception as e:
    print("Cache purge error:", e)

