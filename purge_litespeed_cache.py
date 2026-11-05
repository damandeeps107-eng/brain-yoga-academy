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

# Check wp-admin homepage for LiteSpeed purge link
req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    admin_html = resp.read().decode('utf-8')

purge_links = re.findall(r'href=[\'"]([^\'"]*litespeed[^\'"]*purge[^\'"]*)[\'"]', admin_html)
print("LiteSpeed purge links in admin bar:")
for pl in purge_links:
    print(" ", pl)

# Also check Hostinger cache purge
hostinger_purge = re.findall(r'href=[\'"]([^\'"]*hostinger[^\'"]*purge[^\'"]*)[\'"]', admin_html)
print("Hostinger purge links:", hostinger_purge)

# If purge link found, visit it to clear cache!
if purge_links:
    purge_url = purge_links[0].replace('&amp;', '&')
    if not purge_url.startswith('http'):
        purge_url = 'https://brainyogaacademy.com/wp-admin/' + purge_url
    print("Purging LiteSpeed cache via:", purge_url)
    req = urllib.request.Request(purge_url, headers={'User-Agent': 'Mozilla/5.0'})
    with opener.open(req) as resp:
        print("Purge response code:", resp.status)
