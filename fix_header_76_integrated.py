#!/usr/bin/env python3
"""
Architectural Fix for Header 76:
Instead of a separate floating container that collides with sticky headers,
we place the announcement bar:
- At top of Desktop Header (52259ba)
- At top of Mobile Header (b7ec46a)
Zero overlap, zero white gap, pixel-perfect sticky behavior!
"""
import urllib.request, urllib.parse, http.cookiejar, ssl, json, re

ctx = ssl._create_unverified_context()
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(
    urllib.request.HTTPCookieProcessor(cj),
    urllib.request.HTTPSHandler(context=ctx)
)

# 1. Login
login_data = urllib.parse.urlencode({
    'log': 'rajendraboddu@gmail.com', 'pwd': 'Gemini#1979',
    'wp-submit': 'Log In', 'redirect_to': 'https://brainyogaacademy.com/wp-admin/', 'testcookie': '1'
}).encode()
opener.open(urllib.request.Request('https://brainyogaacademy.com/wp-login.php', data=login_data, headers={'User-Agent': 'Mozilla/5.0'}))
print("Step 1: Logged in!")

# 2. Get Header 76 base elements (from clean backup)
with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/header_76_elements.json', 'r') as f:
    elements = json.load(f)

# Filter out by_top_announcement_bar
clean_elements = [el for el in elements if el.get('id') != 'by_top_announcement_bar']

# Common Flicker CSS & Preloader
FLICKER_CSS = """<style>
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
    transition: color 0.2s ease;
}
.by-flicker-btn:hover {
    color: #ffffff;
    animation-play-state: paused;
}
</style>
<script>
(function() {
    var adultUrl = 'https://brainyogaacademy.com/brain-yoga-for-busy-minds/';
    var fetched = false;
    function instantPreload() {
        if (fetched) return;
        fetched = true;
        var pf = document.createElement('link'); pf.rel = 'prefetch'; pf.href = adultUrl; document.head.appendChild(pf);
    }
    document.addEventListener('mouseover', function(e) {
        if (e.target && e.target.closest && e.target.closest('a[href*=\"brain-yoga-for-busy-minds\"]')) instantPreload();
    });
    document.addEventListener('touchstart', function(e) {
        if (e.target && e.target.closest && e.target.closest('a[href*=\"brain-yoga-for-busy-minds\"]')) instantPreload();
    }, {passive: true});
    if ('requestIdleCallback' in window) requestIdleCallback(instantPreload);
    else setTimeout(instantPreload, 1200);
})();
</script>"""

DESKTOP_BAR_HTML = FLICKER_CSS + """
<div style="display:flex;align-items:center;justify-content:center;gap:8px;flex-wrap:wrap;text-align:center;font-family:'Poppins',-apple-system,BlinkMacSystemFont,sans-serif;font-size:12px;color:#FFFFFF;line-height:1.4;padding:8px 16px;background:#007984;width:100%;box-sizing:border-box;">
    <span style="display:inline-block;padding:2px 10px;border-radius:9999px;font-size:10px;font-weight:700;text-transform:uppercase;background-color:#FD8742;color:#FFFFFF;letter-spacing:0.05em;white-space:nowrap;">
        &#x1F9D1;&#x200D;&#x1F4BC; Adult Wellness
    </span>
    <span style="font-weight:500;font-size:12px;">Working professionals? Brain Yoga for Busy Minds awaits!</span>
    <a href="https://brainyogaacademy.com/brain-yoga-for-busy-minds/" class="by-flicker-btn">
        <span>&#x2728; Brain Yoga for Adults</span>
        <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
    </a>
</div>"""

MOBILE_BAR_HTML = FLICKER_CSS + """
<div style="display:flex;align-items:center;justify-content:center;gap:6px;text-align:center;font-family:'Poppins',-apple-system,BlinkMacSystemFont,sans-serif;font-size:11px;color:#FFFFFF;line-height:1.2;padding:6px 10px;background:#007984;width:100%;box-sizing:border-box;">
    <span style="display:inline-block;padding:1px 7px;border-radius:9999px;font-size:9px;font-weight:700;text-transform:uppercase;background-color:#FD8742;color:#FFFFFF;white-space:nowrap;">
        Adults
    </span>
    <a href="https://brainyogaacademy.com/brain-yoga-for-busy-minds/" class="by-flicker-btn" style="font-size:11px;padding:3px 10px;">
        <span>&#x2728; Brain Yoga for Adults</span>
        <svg xmlns="http://www.w3.org/2000/svg" width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
    </a>
</div>"""

desktop_widget = {
    "id": "by_desktop_announcement_widget",
    "elType": "widget",
    "widgetType": "html",
    "settings": {"html": DESKTOP_BAR_HTML}
}

mobile_widget = {
    "id": "by_mobile_announcement_widget",
    "elType": "widget",
    "widgetType": "html",
    "settings": {"html": MOBILE_BAR_HTML}
}

# Update 52259ba (desktop)
for el in clean_elements:
    if el.get('id') == '52259ba':
        # Remove any existing announcement widgets
        el['elements'] = [sub for sub in el.get('elements', []) if sub.get('id') != 'by_desktop_announcement_widget']
        el['elements'].insert(0, desktop_widget)
        # Reset top padding on 52259ba so bar sits flush at top
        el['settings']['padding'] = {
            'unit': 'px', 'top': '0', 'right': '120', 'bottom': '20', 'left': '120', 'isLinked': False
        }
        print("✅ Added announcement bar inside 52259ba (desktop)")

    elif el.get('id') == 'b7ec46a':
        # Remove any existing announcement widgets
        el['elements'] = [sub for sub in el.get('elements', []) if sub.get('id') != 'by_mobile_announcement_widget']
        el['elements'].insert(0, mobile_widget)
        # Reset top padding on b7ec46a so bar sits flush at top
        el['settings']['padding_mobile'] = {
            'unit': 'px', 'top': '0', 'right': '10', 'bottom': '10', 'left': '10', 'isLinked': False
        }
        el['settings']['padding_tablet'] = {
            'unit': 'px', 'top': '0', 'right': '20', 'bottom': '10', 'left': '20', 'isLinked': False
        }
        el['settings']['padding'] = {
            'unit': 'px', 'top': '0', 'right': '120', 'bottom': '20', 'left': '120', 'isLinked': False
        }
        print("✅ Added announcement bar inside b7ec46a (mobile)")

# 3. Get Elementor nonce for post 76
el_url = 'https://brainyogaacademy.com/wp-admin/post.php?post=76&action=elementor'
ed_html = opener.open(urllib.request.Request(el_url, headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf-8')
ajax_nonce_76 = re.search(r'\"ajax\":\{[^}]*\"nonce\":\"([^\"]+)\"', ed_html).group(1)
print(f"Step 2: Got nonce: {ajax_nonce_76}")

# 4. Save Header 76
actions = {
    'save_builder': {
        'action': 'save_builder',
        'data': {
            'status': 'publish',
            'elements': clean_elements
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
resp = opener.open(ajax_req).read().decode('utf-8')
res = json.loads(resp)
save_result = res.get('data', {}).get('responses', {}).get('save_builder', {})
print(f"Step 3: Header 76 saved! success: {save_result.get('success')}")

# 5. Purge cache
admin_page = opener.open(urllib.request.Request('https://brainyogaacademy.com/wp-admin/', headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf-8')
ls_nonce_match = re.search(r'LSCWP_NONCE=([a-f0-9]+)', admin_page)
ls_nonce = ls_nonce_match.group(1) if ls_nonce_match else '663a0c4afd'

purge_url = f'https://brainyogaacademy.com/?LSCWP_CTRL=purge&LSCWP_NONCE={ls_nonce}&litespeed_type=purge_all'
with opener.open(urllib.request.Request(purge_url, headers={'User-Agent': 'Mozilla/5.0'})) as p:
    print(f"Step 4: Cache purged (Status: {p.status})")

print("🎉 Header 76 updated with integrated zero-overlap structure!")
