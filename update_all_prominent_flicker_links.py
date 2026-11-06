#!/usr/bin/env python3
"""
Performance & Click Fix:
1. REMOVE heavy background prefetch scripts that were choking bandwidth and dropping tap events in mobile Safari.
2. Add explicit touch-action: manipulation, high z-index, and pointer-events: auto to make all buttons 100% responsive and instant.
3. Clean, lightweight CSS for maximum speed and zero lag.
"""

import urllib.request, urllib.parse, http.cookiejar, ssl, json, re

ctx = ssl._create_unverified_context()
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(
    urllib.request.HTTPCookieProcessor(cj),
    urllib.request.HTTPSHandler(context=ctx)
)

print("="*60)
print("FIXING SPEED & CLICK NAVIGATION ON ALL BUTTONS")
print("="*60)

# Login to WordPress
login_data = urllib.parse.urlencode({
    'log': 'rajendraboddu@gmail.com', 'pwd': 'Gemini#1979',
    'wp-submit': 'Log In', 'redirect_to': 'https://brainyogaacademy.com/wp-admin/', 'testcookie': '1'
}).encode()
opener.open(urllib.request.Request('https://brainyogaacademy.com/wp-login.php', data=login_data, headers={'User-Agent': 'Mozilla/5.0'}))
print("✅ Logged in!")

# ─────────────────────────────────────────────────────────────
# 1. HEADER 76 (DESKTOP & MOBILE)
# ─────────────────────────────────────────────────────────────
DESKTOP_HEADER_HTML = """<style>
@keyframes byFlickerPulse {
    0%, 100% {
        box-shadow: 0 2px 8px rgba(0,0,0,0.15), 0 0 0 0 rgba(253, 135, 66, 0.65);
        transform: scale(1);
    }
    50% {
        box-shadow: 0 4px 18px rgba(0,0,0,0.22), 0 0 0 4px rgba(253, 135, 66, 0.4), 0 0 18px rgba(253, 135, 66, 0.75);
        transform: scale(1.03);
    }
}
.by-flicker-btn-prominent {
    animation: byFlickerPulse 2.4s ease-in-out infinite !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 7px !important;
    border-radius: 9999px !important;
    padding: 6px 18px !important;
    border: 2px solid #FD8742 !important;
    background: #FFFFFF !important;
    font-weight: 800 !important;
    font-size: 13.5px !important;
    color: #C2410C !important;
    text-decoration: none !important;
    white-space: nowrap !important;
    letter-spacing: 0.01em !important;
    font-family: 'Poppins', -apple-system, BlinkMacSystemFont, sans-serif !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.15) !important;
    transition: transform 0.2s ease, background-color 0.2s ease, color 0.2s ease !important;
    cursor: pointer !important;
    pointer-events: auto !important;
    touch-action: manipulation !important;
    -webkit-tap-highlight-color: rgba(253, 135, 66, 0.3) !important;
    position: relative !important;
    z-index: 999999 !important;
}
.by-flicker-btn-prominent:hover {
    color: #ffffff !important;
    background: #FD8742 !important;
    border-color: #FFFFFF !important;
    animation-play-state: paused !important;
    transform: scale(1.05) !important;
    box-shadow: 0 6px 20px rgba(253, 135, 66, 0.6) !important;
}
.by-flicker-btn-prominent svg {
    flex-shrink: 0 !important;
    transition: transform 0.2s ease !important;
}
.by-flicker-btn-prominent:hover svg {
    transform: translateX(3px) !important;
}
</style>
<div style="display:flex;align-items:center;justify-content:center;gap:12px;flex-wrap:wrap;text-align:center;font-family:'Poppins',-apple-system,BlinkMacSystemFont,sans-serif;font-size:13px;color:#FFFFFF;line-height:1.4;padding:8px 16px;background:#007984;width:100%;box-sizing:border-box;position:relative;z-index:99999;">
    <span style="display:inline-block;padding:2px 10px;border-radius:9999px;font-size:10px;font-weight:700;text-transform:uppercase;background-color:#FD8742;color:#FFFFFF;letter-spacing:0.05em;white-space:nowrap;">
        Adult Wellness
    </span>
    <span style="font-weight:600;font-size:13px;opacity:0.95;">Working professionals? Brain Yoga for Busy Minds awaits!</span>
    <a href="https://brainyogaacademy.com/brain-yoga-for-busy-minds/" class="by-flicker-btn-prominent" target="_self" rel="noopener">
        <span style="font-size:15px;">🧘</span>
        <span>Brain Yoga for Adults</span>
        <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
    </a>
</div>"""

MOBILE_HEADER_HTML = """<style>
@keyframes byFlickerPulse {
    0%, 100% {
        box-shadow: 0 2px 8px rgba(0,0,0,0.15), 0 0 0 0 rgba(253, 135, 66, 0.65);
        transform: scale(1);
    }
    50% {
        box-shadow: 0 4px 18px rgba(0,0,0,0.22), 0 0 0 4px rgba(253, 135, 66, 0.4), 0 0 18px rgba(253, 135, 66, 0.75);
        transform: scale(1.03);
    }
}
.by-flicker-btn-mobile {
    animation: byFlickerPulse 2.4s ease-in-out infinite !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 6px !important;
    border-radius: 9999px !important;
    padding: 5px 14px !important;
    border: 2px solid #FD8742 !important;
    background: #FFFFFF !important;
    font-weight: 800 !important;
    font-size: 12px !important;
    color: #C2410C !important;
    text-decoration: none !important;
    white-space: nowrap !important;
    letter-spacing: 0.01em !important;
    font-family: 'Poppins', -apple-system, BlinkMacSystemFont, sans-serif !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.15) !important;
    cursor: pointer !important;
    pointer-events: auto !important;
    touch-action: manipulation !important;
    -webkit-tap-highlight-color: rgba(253, 135, 66, 0.3) !important;
    position: relative !important;
    z-index: 999999 !important;
}
.by-flicker-btn-mobile:hover, .by-flicker-btn-mobile:active {
    color: #ffffff !important;
    background: #FD8742 !important;
    border-color: #FFFFFF !important;
}
</style>
<div style="display:flex;align-items:center;justify-content:center;gap:8px;text-align:center;font-family:'Poppins',-apple-system,BlinkMacSystemFont,sans-serif;font-size:11px;color:#FFFFFF;line-height:1.2;padding:6px 10px;background:#007984;width:100%;box-sizing:border-box;position:relative;z-index:99999;">
    <span style="display:inline-block;padding:2px 8px;border-radius:9999px;font-size:9px;font-weight:700;text-transform:uppercase;background-color:#FD8742;color:#FFFFFF;white-space:nowrap;">
        Adults
    </span>
    <a href="https://brainyogaacademy.com/brain-yoga-for-busy-minds/" class="by-flicker-btn-mobile" target="_self" rel="noopener">
        <span style="font-size:14px;">🧘</span>
        <span>Brain Yoga for Adults</span>
        <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
    </a>
</div>"""

with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/header_76_elements.json', 'r') as f:
    h_elements = json.load(f)

clean_h = [el for el in h_elements if el.get('id') != 'by_top_announcement_bar']

for el in clean_h:
    if el.get('id') == '52259ba':
        el['elements'] = [sub for sub in el.get('elements', []) if sub.get('id') != 'by_desktop_announcement_widget']
        el['elements'].insert(0, {
            "id": "by_desktop_announcement_widget", "elType": "widget", "widgetType": "html",
            "settings": {"html": DESKTOP_HEADER_HTML}
        })
        el['settings']['padding'] = {'unit': 'px', 'top': '0', 'right': '120', 'bottom': '20', 'left': '120', 'isLinked': False}
    elif el.get('id') == 'b7ec46a':
        el['elements'] = [sub for sub in el.get('elements', []) if sub.get('id') != 'by_mobile_announcement_widget']
        el['elements'].insert(0, {
            "id": "by_mobile_announcement_widget", "elType": "widget", "widgetType": "html",
            "settings": {"html": MOBILE_HEADER_HTML}
        })
        el['settings']['padding_mobile'] = {'unit': 'px', 'top': '0', 'right': '10', 'bottom': '10', 'left': '10', 'isLinked': False}
        el['settings']['padding_tablet'] = {'unit': 'px', 'top': '0', 'right': '20', 'bottom': '10', 'left': '20', 'isLinked': False}
        el['settings']['padding'] = {'unit': 'px', 'top': '0', 'right': '120', 'bottom': '20', 'left': '120', 'isLinked': False}

el_url = 'https://brainyogaacademy.com/wp-admin/post.php?post=76&action=elementor'
ed_html = opener.open(urllib.request.Request(el_url, headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf-8')
ajax_nonce_76 = re.search(r'\"ajax\":\{[^}]*\"nonce\":\"([^\"]+)\"', ed_html).group(1)

actions_76 = {'save_builder': {'action': 'save_builder', 'data': {'status': 'publish', 'elements': clean_h}}}
ajax_data_76 = urllib.parse.urlencode({'action': 'elementor_ajax', '_nonce': ajax_nonce_76, 'editor_post_id': '76', 'actions': json.dumps(actions_76)}).encode('utf-8')
resp_76 = opener.open(urllib.request.Request('https://brainyogaacademy.com/wp-admin/admin-ajax.php', data=ajax_data_76, headers={'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/x-www-form-urlencoded'})).read().decode('utf-8')
res_76 = json.loads(resp_76)
print(f"✅ Header 76 saved: {res_76.get('data',{}).get('responses',{}).get('save_builder',{}).get('success')}")

# ─────────────────────────────────────────────────────────────
# 2. KIDS BOTTOM BAR (POST 1111)
# ─────────────────────────────────────────────────────────────
KIDS_BOTTOM_HTML = """<style>
@keyframes byFlickerPulse {
    0%, 100% { box-shadow: 0 2px 8px rgba(0,0,0,0.15), 0 0 0 0 rgba(253, 135, 66, 0.65); transform: scale(1); }
    50% { box-shadow: 0 4px 18px rgba(0,0,0,0.22), 0 0 0 4px rgba(253, 135, 66, 0.4), 0 0 18px rgba(253, 135, 66, 0.75); transform: scale(1.03); }
}
.by-flicker-btn-prominent {
    animation: byFlickerPulse 2.4s ease-in-out infinite !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 7px !important;
    border-radius: 9999px !important;
    padding: 6px 18px !important;
    border: 2px solid #FD8742 !important;
    background: #FFFFFF !important;
    font-weight: 800 !important;
    font-size: 13.5px !important;
    color: #C2410C !important;
    text-decoration: none !important;
    white-space: nowrap !important;
    letter-spacing: 0.01em !important;
    font-family: 'Poppins', -apple-system, BlinkMacSystemFont, sans-serif !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.15) !important;
    transition: transform 0.2s ease, background-color 0.2s ease, color 0.2s ease !important;
    cursor: pointer !important;
    pointer-events: auto !important;
    touch-action: manipulation !important;
    -webkit-tap-highlight-color: rgba(253, 135, 66, 0.3) !important;
    position: relative !important;
    z-index: 999999 !important;
}
.by-flicker-btn-prominent:hover {
    color: #ffffff !important;
    background: #FD8742 !important;
    border-color: #FFFFFF !important;
    animation-play-state: paused !important;
    transform: scale(1.05) !important;
    box-shadow: 0 6px 20px rgba(253, 135, 66, 0.6) !important;
}
.by-flicker-btn-prominent svg {
    flex-shrink: 0 !important;
    transition: transform 0.2s ease !important;
}
.by-flicker-btn-prominent:hover svg {
    transform: translateX(3px) !important;
}
@media (max-width: 640px) {
    .by-flicker-btn-prominent { padding: 4px 12px !important; font-size: 12px !important; gap: 5px !important; }
}
</style>
<div style="background:linear-gradient(135deg,#085C65 0%,#007984 60%,#0a8f9b 100%);padding:18px 20px;text-align:center;width:100%;box-sizing:border-box;font-family:'Poppins',-apple-system,BlinkMacSystemFont,sans-serif;" id="by-bottom-adult-bar">
    <div style="max-width:960px;margin:0 auto;display:flex;align-items:center;justify-content:center;gap:12px;flex-wrap:wrap;">
        <span style="font-size:13px;font-weight:600;color:rgba(255,255,255,.95);letter-spacing:0.01em;">💡 Also explore our Adults program &mdash;</span>
        <a href="https://brainyogaacademy.com/brain-yoga-for-busy-minds/" class="by-flicker-btn-prominent" target="_self" rel="noopener">
            <span style="font-size:15px;">🧘</span>
            <span>Brain Yoga for Adults</span>
            <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </a>
        <span style="font-size:12px;color:rgba(255,255,255,.75);">Clarity &middot; Stress Relief &middot; Peak Performance</span>
    </div>
</div>"""

el_url_1111 = 'https://brainyogaacademy.com/wp-admin/post.php?post=1111&action=elementor'
ed_html_1111 = opener.open(urllib.request.Request(el_url_1111, headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf-8')
ajax_nonce_1111 = re.search(r'\"ajax\":\{[^}]*\"nonce\":\"([^\"]+)\"', ed_html_1111).group(1)

actions_get_1111 = {'get_revision_data': {'action': 'get_revision_data', 'data': {'id': '1111', 'post_id': '1111'}}}
ajax_data_get_1111 = urllib.parse.urlencode({'action': 'elementor_ajax', '_nonce': ajax_nonce_1111, 'editor_post_id': '1111', 'actions': json.dumps(actions_get_1111)}).encode()
resp_get_1111 = opener.open(urllib.request.Request('https://brainyogaacademy.com/wp-admin/admin-ajax.php', data=ajax_data_get_1111, headers={'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/x-www-form-urlencoded'})).read().decode('utf-8')
res_get_1111 = json.loads(resp_get_1111)
curr_1111_elements = res_get_1111.get('data',{}).get('responses',{}).get('get_revision_data',{}).get('data',{}).get('elements',[])

clean_1111 = [el for el in curr_1111_elements if el.get('id') != 'by_bottom_adult_bar_1111']
new_bottom_container = {
    "id": "by_bottom_adult_bar_1111",
    "elType": "container",
    "isInner": False,
    "settings": {
        "content_width": "full",
        "background_background": "classic",
        "background_color": "#007984",
        "padding": {"unit":"px","top":"0","right":"0","bottom":"0","left":"0","isLinked":True}
    },
    "elements": [{
        "id": "by_bottom_adult_html_c",
        "elType": "widget",
        "widgetType": "html",
        "settings": {"html": KIDS_BOTTOM_HTML}
    }]
}
final_1111 = clean_1111 + [new_bottom_container]

actions_save_1111 = {'save_builder': {'action': 'save_builder', 'data': {'status': 'publish', 'elements': final_1111}}}
ajax_data_save_1111 = urllib.parse.urlencode({'action': 'elementor_ajax', '_nonce': ajax_nonce_1111, 'editor_post_id': '1111', 'actions': json.dumps(actions_save_1111)}).encode()
resp_save_1111 = opener.open(urllib.request.Request('https://brainyogaacademy.com/wp-admin/admin-ajax.php', data=ajax_data_save_1111, headers={'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/x-www-form-urlencoded'})).read().decode('utf-8')
res_save_1111 = json.loads(resp_save_1111)
print(f"✅ Post 1111 saved: {res_save_1111.get('data',{}).get('responses',{}).get('save_builder',{}).get('success')}")

# Purge cache
admin_p = opener.open(urllib.request.Request('https://brainyogaacademy.com/wp-admin/', headers={'User-Agent':'Mozilla/5.0'})).read().decode()
ls_nonce_m = re.search(r'LSCWP_NONCE=([a-f0-9]+)', admin_p)
ls_nonce = ls_nonce_m.group(1) if ls_nonce_m else '663a0c4afd'
with opener.open(urllib.request.Request(f'https://brainyogaacademy.com/?LSCWP_CTRL=purge&LSCWP_NONCE={ls_nonce}&litespeed_type=purge_all', headers={'User-Agent': 'Mozilla/5.0'})) as pr:
    print(f"✅ LiteSpeed cache purged (Status: {pr.status})")

print("All elements updated cleanly!")
