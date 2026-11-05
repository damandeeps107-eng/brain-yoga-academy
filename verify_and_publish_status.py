import urllib.request, urllib.parse, http.cookiejar, ssl, json, re

ctx = ssl._create_unverified_context()

# 1. Test anonymous public access
public_url = 'https://brainyogaacademy.com/brain-yoga-for-busy-minds/'
print("Checking anonymous public access to:", public_url)
try:
    req = urllib.request.Request(public_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, context=ctx) as resp:
        print("Public response status:", resp.status)
        print("Final URL:", resp.geturl())
except urllib.error.HTTPError as e:
    print("HTTPError:", e.code, e.reason)
except Exception as e:
    print("Error:", e)

# 2. Login to WP Admin to inspect post status and publish if needed
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

# Check WP REST API for Post 1242
rest_url = 'https://brainyogaacademy.com/wp-json/wp/v2/pages/1242'
req = urllib.request.Request(rest_url, headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    post_data = json.loads(resp.read().decode('utf-8'))
    print("Current WP post status:", post_data.get('status'))
    print("Current permalink / link:", post_data.get('link'))
    print("Current slug:", post_data.get('slug'))

# If not published, publish via REST API or post edit
if post_data.get('status') != 'publish':
    print("Publishing Post 1242 via WP Admin...")
    # Get wp nonce from edit page
    edit_url = 'https://brainyogaacademy.com/wp-admin/post.php?post=1242&action=edit'
    req = urllib.request.Request(edit_url, headers={'User-Agent': 'Mozilla/5.0'})
    with opener.open(req) as resp:
        edit_html = resp.read().decode('utf-8')
    
    # Extract wp-rest nonce or post edit nonce
    rest_nonce_m = re.search(r'\"nonce\":\"([^\"]+)\"', edit_html)
    wpnonce_m = re.search(r'id=\"_wpnonce\" name=\"_wpnonce\" value=\"([^\"]+)\"', edit_html)
    
    # Method A: REST API update with _wpnonce
    wp_api_settings_m = re.search(r'wpApiSettings\s*=\s*\{[^}]*\"nonce\":\"([^\"]+)\"', edit_html)
    if wp_api_settings_m:
        rest_nonce = wp_api_settings_m.group(1)
        print("Got wpApiSettings nonce:", rest_nonce)
        patch_data = json.dumps({'status': 'publish'}).encode('utf-8')
        patch_req = urllib.request.Request(
            rest_url,
            data=patch_data,
            headers={
                'User-Agent': 'Mozilla/5.0',
                'Content-Type': 'application/json',
                'X-WP-Nonce': rest_nonce
            },
            method='POST'
        )
        try:
            with opener.open(patch_req) as resp:
                res = json.loads(resp.read().decode('utf-8'))
                print("REST API Publish Success! Status:", res.get('status'), "Link:", res.get('link'))
        except Exception as e:
            print("REST API update failed:", e)
    
    # Method B: If still not published, use classic form post
    req = urllib.request.Request(rest_url, headers={'User-Agent': 'Mozilla/5.0'})
    with opener.open(req) as resp:
        post_data = json.loads(resp.read().decode('utf-8'))
        print("Post status after REST update:", post_data.get('status'))
        if post_data.get('status') != 'publish' and wpnonce_m:
            wpnonce = wpnonce_m.group(1)
            print("Trying post.php form submit with _wpnonce:", wpnonce)
            form_data = urllib.parse.urlencode({
                '_wpnonce': wpnonce,
                '_wp_http_referer': '/wp-admin/post.php?post=1242&action=edit',
                'action': 'editpost',
                'post_ID': '1242',
                'post_type': 'page',
                'post_status': 'publish',
                'publish': 'Publish',
                'original_post_status': 'draft'
            }).encode('utf-8')
            req = urllib.request.Request(
                'https://brainyogaacademy.com/wp-admin/post.php',
                data=form_data,
                headers={'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/x-www-form-urlencoded'}
            )
            with opener.open(req) as resp:
                print("Form submit response code:", resp.status)

# Final test of anonymous public access
print("\n--- Final Anonymous Public Access Verification ---")
try:
    req = urllib.request.Request(public_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, context=ctx) as resp:
        print("FINAL Public Status:", resp.status)
        print("FINAL Public URL:", resp.geturl())
except Exception as e:
    print("Final check error:", e)
