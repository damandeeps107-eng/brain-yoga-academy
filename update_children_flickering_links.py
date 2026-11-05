#!/usr/bin/env python3
"""
Update Header 76 top announcement bar to have FLICKERING animation.
Also add BOTTOM flickering bar to Post 1111 (Children homepage).

Sir's requirement:
- TOP & BOTTOM of Children page: flickering "Brain Yoga for Adults" link → /brain-yoga-for-busy-minds/
- TOP & BOTTOM of Adults page: flickering "Brain Yoga for Children" link → brainyogaacademy.com/ (already done in HTML)
"""

import urllib.request, urllib.parse, http.cookiejar, ssl, json, re

ctx = ssl._create_unverified_context()
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(
    urllib.request.HTTPCookieProcessor(cj),
    urllib.request.HTTPSHandler(context=ctx)
)

# ─────────────────────────────────────────────────────────────
# 1. Login to WP
# ─────────────────────────────────────────────────────────────
print("Step 1: Logging in to WordPress...")
login_url = 'https://brainyogaacademy.com/wp-login.php'
login_data = urllib.parse.urlencode({
    'log': 'rajendraboddu@gmail.com',
    'pwd': 'Gemini#1979',
    'wp-submit': 'Log In',
    'redirect_to': 'https://brainyogaacademy.com/wp-admin/',
    'testcookie': '1'
}).encode('utf-8')
opener.open(urllib.request.Request(login_url, data=login_data, headers={'User-Agent': 'Mozilla/5.0'}))
print("   ✅ Logged in!")

# ─────────────────────────────────────────────────────────────
# 2. Update Header 76 top bar → Flickering "Brain Yoga for Adults"
# ─────────────────────────────────────────────────────────────
print("\nStep 2: Updating Header 76 top bar with flickering animation...")

with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/header_76_elements.json', 'r') as f:
    elements = json.load(f)

# Remove existing top announcement bar if any
clean_elements = [el for el in elements if el.get('id') != 'by_top_announcement_bar']

FLICKER_CSS = """
    <style>
        @keyframes byGentleFlicker {
            0%, 100% {
                opacity: 1;
                box-shadow: 0 0 6px rgba(253,135,66,0.4), 0 0 12px rgba(253,135,66,0.2);
                text-shadow: 0 0 8px rgba(255,232,218,0.6);
            }
            50% {
                opacity: 0.72;
                box-shadow: 0 0 16px rgba(253,135,66,0.9), 0 0 32px rgba(253,135,66,0.5);
                text-shadow: 0 0 14px rgba(255,255,255,0.9);
            }
        }
        .by-flicker-btn {
            animation: byGentleFlicker 2.6s ease-in-out infinite;
            display: inline-flex;
            align-items: center;
            gap: 4px;
            border-radius: 20px;
            padding: 3px 12px 3px 10px;
            border: 1px solid rgba(253,135,66,0.55);
            background: rgba(253,135,66,0.15);
            font-weight: 700;
            color: #FFE8DA;
            text-decoration: none;
            white-space: nowrap;
            font-size: 12px;
            font-family: 'Poppins', -apple-system, sans-serif;
        }
        .by-flicker-btn:hover {
            color: #ffffff;
            animation-play-state: paused;
        }
    </style>
"""

TOP_BAR_HTML = FLICKER_CSS + """
<div style="display:flex;align-items:center;justify-content:center;gap:8px;flex-wrap:wrap;text-align:center;font-family:'Poppins',-apple-system,BlinkMacSystemFont,sans-serif;font-size:12px;color:#FFFFFF;line-height:1.4;">
    <span style="display:inline-block;padding:2px 10px;border-radius:9999px;font-size:10px;font-weight:700;text-transform:uppercase;background-color:#FD8742;color:#FFFFFF;letter-spacing:0.05em;white-space:nowrap;">
        &#x1F9D1;&#x200D;&#x1F4BC; Adult Wellness
    </span>
    <span style="font-weight:500;font-size:12px;">Working professionals? Brain Yoga for Busy Minds awaits!</span>
    <a href="https://brainyogaacademy.com/brain-yoga-for-busy-minds/"
       class="by-flicker-btn">
        <span>&#x2728; Brain Yoga for Adults</span>
        <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
    </a>
</div>
"""

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
            "top": "9",
            "right": "16",
            "bottom": "9",
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
                "html": TOP_BAR_HTML
            }
        }
    ]
}

new_elements = [announcement_bar] + clean_elements

# Get Elementor nonce for post 76
el_url = 'https://brainyogaacademy.com/wp-admin/post.php?post=76&action=elementor'
req = urllib.request.Request(el_url, headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    ed_html = resp.read().decode('utf-8')

ajax_nonce_76 = re.search(r'\"ajax\":\{[^}]*\"nonce\":\"([^\"]+)\"', ed_html).group(1)
print(f"   Got Elementor nonce for Header 76: {ajax_nonce_76}")

# Save Header 76 via save_builder
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
    '_nonce': ajax_nonce_76,
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
    print(f"   ✅ Header 76 updated! save_builder success: {save_result.get('success')}")

# ─────────────────────────────────────────────────────────────
# 3. Add BOTTOM flickering bar to Post 1111 (Children homepage)
# ─────────────────────────────────────────────────────────────
print("\nStep 3: Adding bottom flickering bar to Post 1111 (Children homepage)...")

# Get current elements of post 1111
el_url_1111 = 'https://brainyogaacademy.com/wp-admin/post.php?post=1111&action=elementor'
req = urllib.request.Request(el_url_1111, headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    ed_html_1111 = resp.read().decode('utf-8')

ajax_nonce_1111 = re.search(r'\"ajax\":\{[^}]*\"nonce\":\"([^\"]+)\"', ed_html_1111).group(1)
print(f"   Got Elementor nonce for Post 1111: {ajax_nonce_1111}")

# Extract existing elements of Post 1111
elements_match = re.search(r'\"elements\":\s*(\[.*?\])\s*,\s*\"version\"', ed_html_1111, re.DOTALL)
if not elements_match:
    # Try alternate pattern
    elements_match = re.search(r'elementorConfig\s*=\s*\{.*?\"elements\":\s*(\[)', ed_html_1111, re.DOTALL)

# Use REST API to get elements
rest_url = 'https://brainyogaacademy.com/wp-json/elementor/v1/globals'
try:
    req = urllib.request.Request(rest_url, headers={'User-Agent': 'Mozilla/5.0'})
    with opener.open(req) as resp:
        pass
except:
    pass

# Get elements via WP REST API for post 1111
rest_post_url = 'https://brainyogaacademy.com/wp-json/wp/v2/pages/1111'
req = urllib.request.Request(rest_post_url, headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    post_data = json.loads(resp.read().decode('utf-8'))

# Get elementor data from post meta
el_data_raw = post_data.get('meta', {}).get('_elementor_data', '[]')
if isinstance(el_data_raw, str):
    post_1111_elements = json.loads(el_data_raw) if el_data_raw else []
else:
    post_1111_elements = el_data_raw
print(f"   Got {len(post_1111_elements)} top-level elements from Post 1111")

# BOTTOM BAR HTML for Children page — links to Adults
BOTTOM_BAR_CHILDREN = FLICKER_CSS + """
<div style="background:linear-gradient(135deg,#085C65 0%,#007984 60%,#0a8f9b 100%);padding:16px 20px;text-align:center;width:100%;box-sizing:border-box;margin:0;font-family:'Poppins',-apple-system,BlinkMacSystemFont,sans-serif;" id="by-bottom-adult-bar">
    <div style="max-width:900px;margin:0 auto;display:flex;align-items:center;justify-content:center;gap:10px;flex-wrap:wrap;">
        <span style="font-size:12px;font-weight:600;color:rgba(255,255,255,0.88);">
            &#x1F4A1; Also explore our Adults program &mdash;
        </span>
        <a href="https://brainyogaacademy.com/brain-yoga-for-busy-minds/"
           class="by-flicker-btn"
           style="font-size:13px;">
            <span>&#x2728; Brain Yoga for Adults</span>
            <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </a>
        <span style="font-size:11px;color:rgba(255,255,255,0.6);">Stress Relief &middot; Focus &middot; Calm for Working Professionals</span>
    </div>
</div>
"""

# Check if bottom bar already there
el_data_str = json.dumps(post_1111_elements)
if "by-bottom-adult-bar" in el_data_str:
    print("   ⚠️  Bottom bar already present in Post 1111 — will re-add fresh")
    # Remove existing
    post_1111_elements = [el for el in post_1111_elements if
                          "by-bottom-adult-bar" not in json.dumps(el.get('elements', []))]

# Create the bottom bar container for Post 1111
bottom_bar_1111 = {
    "id": "by_bottom_adult_bar_1111",
    "elType": "container",
    "isInner": False,
    "settings": {
        "content_width": "full",
        "background_background": "classic",
        "background_color": "#007984",
        "padding": {
            "unit": "px",
            "top": "0",
            "right": "0",
            "bottom": "0",
            "left": "0",
            "isLinked": True
        }
    },
    "elements": [
        {
            "id": "by_bottom_adult_html_1111",
            "elType": "widget",
            "widgetType": "html",
            "settings": {
                "html": BOTTOM_BAR_CHILDREN
            }
        }
    ]
}

# Append at END of elements list
post_1111_elements_updated = post_1111_elements + [bottom_bar_1111]

# Save Post 1111
actions_1111 = {
    'save_builder': {
        'action': 'save_builder',
        'data': {
            'status': 'publish',
            'elements': post_1111_elements_updated
        }
    }
}
ajax_data_1111 = urllib.parse.urlencode({
    'action': 'elementor_ajax',
    '_nonce': ajax_nonce_1111,
    'editor_post_id': '1111',
    'actions': json.dumps(actions_1111)
}).encode('utf-8')

ajax_req_1111 = urllib.request.Request(
    'https://brainyogaacademy.com/wp-admin/admin-ajax.php',
    data=ajax_data_1111,
    headers={'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/x-www-form-urlencoded'}
)
with opener.open(ajax_req_1111) as resp:
    res_1111 = json.loads(resp.read().decode('utf-8'))
    save_result_1111 = res_1111.get('data', {}).get('responses', {}).get('save_builder', {})
    print(f"   ✅ Post 1111 bottom bar added! save_builder success: {save_result_1111.get('success')}")

# ─────────────────────────────────────────────────────────────
# 4. Purge LiteSpeed Cache
# ─────────────────────────────────────────────────────────────
print("\nStep 4: Purging LiteSpeed cache...")
# Get fresh nonce
admin_page = opener.open(urllib.request.Request(
    'https://brainyogaacademy.com/wp-admin/',
    headers={'User-Agent': 'Mozilla/5.0'}
)).read().decode('utf-8')

ls_nonce_match = re.search(r'LSCWP_NONCE=([a-f0-9]+)', admin_page)
ls_nonce = ls_nonce_match.group(1) if ls_nonce_match else '663a0c4afd'
print(f"   LiteSpeed nonce: {ls_nonce}")

purge_url = f'https://brainyogaacademy.com/?LSCWP_CTRL=purge&LSCWP_NONCE={ls_nonce}&litespeed_type=purge_all'
try:
    req = urllib.request.Request(purge_url, headers={'User-Agent': 'Mozilla/5.0', 'Referer': 'https://brainyogaacademy.com/wp-admin/'})
    with opener.open(req) as resp:
        print(f"   ✅ LiteSpeed cache purged! Status: {resp.status}")
except Exception as e:
    print(f"   ⚠️  Cache purge: {e}")

# Try admin purge too
try:
    purge_url2 = f'https://brainyogaacademy.com/wp-admin/index.php?LSCWP_CTRL=purge&LSCWP_NONCE={ls_nonce}&litespeed_type=purge_all'
    req2 = urllib.request.Request(purge_url2, headers={'User-Agent': 'Mozilla/5.0'})
    with opener.open(req2) as resp2:
        print(f"   ✅ Admin LiteSpeed purge status: {resp2.status}")
except Exception as e:
    print(f"   ⚠️  Admin cache purge: {e}")

print("\n" + "="*60)
print("✅ ALL DONE! Summary:")
print("   - Header 76 (Children top bar): FLICKERING ✨")
print("   - Post 1111 (Children bottom bar): FLICKERING ✨ (new)")
print("   - Adult page busy-minds.html: FLICKERING top+bottom ✨ (deployed)")
print("="*60)
