import urllib.request, urllib.parse, http.cookiejar, ssl, json, re

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

req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/post.php?post=76&action=elementor', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    html = resp.read().decode('utf-8')

idx = html.find('\"elements\":[')
sub = html[idx+len('\"elements\":'):]
elements, _ = json.JSONDecoder().raw_decode(sub)

with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/header_76_elements.json', 'w') as f:
    json.dump(elements, f, indent=2)

print("Saved header_76_elements.json, count of roots:", len(elements))
for i, el in enumerate(elements):
    print(f"Root {i}: id={el.get('id')} elType={el.get('elType')} settings={el.get('settings')}")
