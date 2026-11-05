import urllib.request, urllib.parse, http.cookiejar, ssl, re

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

# Check revisions of Post 76
req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/revision.php?post=76', headers={'User-Agent': 'Mozilla/5.0'})
try:
    with opener.open(req) as resp:
        html = resp.read().decode('utf-8')
        revs = re.findall(r'from=(\d+)&to=(\d+)', html)
        print("Revisions found for post 76:", revs)
        # Find restore link
        restore_links = re.findall(r'href=[\'"]([^\'"]*action=restore[^\'"]*)[\'"]', html)
        print("Restore links:", restore_links)
except Exception as e:
    print("Error checking revisions:", e)

# Also check Elementor revisions endpoint
el_url = 'https://brainyogaacademy.com/wp-admin/post.php?post=76&action=elementor'
with opener.open(urllib.request.Request(el_url, headers={'User-Agent': 'Mozilla/5.0'})) as resp:
    html = resp.read().decode('utf-8')
    rev_matches = re.findall(r'\"revisions\":(\[.*?\])', html)
    if rev_matches:
        print("Elementor revisions in post 76:", rev_matches[0][:500])
