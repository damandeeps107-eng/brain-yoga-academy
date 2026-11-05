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

# Check wp-admin/edit.php?post_type=page to find Post 1242 and its publish nonce!
req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/edit.php?post_type=page', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    pages_html = resp.read().decode('utf-8')

# Search for 1242 in pages_html
m = re.findall(r'<tr[^>]*id=\"post-1242\"[^>]*>.*?</tr>', pages_html, re.DOTALL)
if m:
    print("Found post-1242 row in edit.php:")
    print(m[0][:500])
    # Find links inside this row (edit, inline-edit, trash, view)
    links = re.findall(r'href=[\'"]([^\'"]+)[\'"]', m[0])
    for l in links:
        print("Link:", l)
else:
    print("Post 1242 not found in first page of edit.php, searching drafts...")
    req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/edit.php?post_status=draft&post_type=page', headers={'User-Agent': 'Mozilla/5.0'})
    with opener.open(req) as resp:
        drafts_html = resp.read().decode('utf-8')
    m = re.findall(r'<tr[^>]*id=\"post-1242\"[^>]*>.*?</tr>', drafts_html, re.DOTALL)
    if m:
        print("Found post-1242 in drafts:")
        print(m[0][:500])
        links = re.findall(r'href=[\'"]([^\'"]+)[\'"]', m[0])
        for l in links:
            print("Link:", l)
