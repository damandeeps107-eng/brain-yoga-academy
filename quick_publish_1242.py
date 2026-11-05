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

# Get edit.php
req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/edit.php?post_type=page', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    html = resp.read().decode('utf-8')

# Search for inline edit nonce
nonce_m = re.search(r'id=\"_inline_edit\" name=\"_inline_edit\" value=\"([^\"]+)\"', html)
if nonce_m:
    inline_nonce = nonce_m.group(1)
    print("Found inline_edit nonce:", inline_nonce)

    # Perform quick edit to publish post 1242
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
        'page_template': 'elementor_header_footer'
    }).encode('utf-8')

    ajax_req = urllib.request.Request(
        'https://brainyogaacademy.com/wp-admin/admin-ajax.php',
        data=quick_data,
        headers={'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/x-www-form-urlencoded'}
    )
    with opener.open(ajax_req) as resp:
        result_html = resp.read().decode('utf-8')
        print("Quick edit response preview:")
        print(result_html[:400])
        if 'status-publish' in result_html:
            print("CONFIRMED: Post 1242 is now status-publish!")
        else:
            print("Status in response:", re.findall(r'status-[a-z]+', result_html))
else:
    print("Could not find _inline_edit nonce in edit.php")
