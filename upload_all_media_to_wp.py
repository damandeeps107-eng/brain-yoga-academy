import urllib.request, urllib.parse, http.cookiejar, ssl, json, re, os

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

# Get nonce
req = urllib.request.Request('https://brainyogaacademy.com/wp-admin/post.php?post=1242&action=edit', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(req) as resp:
    html = resp.read().decode('utf-8')
api_nonce = re.search(r'wpApiSettings\s*=\s*\{[^}]*\"nonce\":\"([^\"]+)\"', html).group(1)

IMAGE_FILES = [
    'rajendra_14_new.webp',
    'trainer_rajendra_portrait.jpg',
    'barking_dog_new.webp',
    'practice_braingym.webp',
    'practice_ambidextrous.webp',
    'practice_pranayama.webp',
    'practice_mindfulness.webp',
    'practice_visualization.webp',
    'practice_eft.webp',
    'practice_yoganidra.webp',
    'practice_awareness.webp',
    'workshop_corporate_team.webp',
    'workshop_corporate_chair.webp',
    'testimonial_uma.jpg',
    'testimonial_aryan.jpg',
    'testimonial_kavitha.jpg',
    'testimonial_sravani.jpg',
    'testimonial_vinay.jpg',
    'testimonial_kiran.jpg',
    'official_logo.png'
]

LOCAL_DIR = '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing'
MEDIA_MAP_FILE = os.path.join(LOCAL_DIR, 'wp_media_map.json')

media_map = {}
if os.path.exists(MEDIA_MAP_FILE):
    try:
        with open(MEDIA_MAP_FILE, 'r') as f:
            media_map = json.load(f)
    except:
        pass

for fname in IMAGE_FILES:
    if fname in media_map:
        print(f"[CACHED] {fname} -> ID: {media_map[fname]['id']}, URL: {media_map[fname]['url']}")
        continue

    local_path = os.path.join(LOCAL_DIR, fname)
    if not os.path.exists(local_path):
        print(f"[MISSING LOCAL] {fname}")
        continue

    # Check if already in WP
    search_stem = os.path.splitext(fname)[0]
    check_req = urllib.request.Request(
        f'https://brainyogaacademy.com/wp-json/wp/v2/media?search={urllib.parse.quote(search_stem)}',
        headers={'User-Agent': 'Mozilla/5.0', 'X-WP-Nonce': api_nonce}
    )
    already = None
    try:
        with opener.open(check_req) as resp:
            results = json.loads(resp.read().decode('utf-8'))
            for r in results:
                if fname in r.get('source_url', ''):
                    already = r
                    break
    except Exception as e:
        print(f"Error checking {fname}: {e}")

    if already:
        media_map[fname] = {'id': already['id'], 'url': already['source_url']}
        print(f"[FOUND ON WP] {fname} -> ID: {already['id']}, URL: {already['source_url']}")
    else:
        # Upload
        mime = 'image/webp' if fname.endswith('.webp') else ('image/png' if fname.endswith('.png') else 'image/jpeg')
        with open(local_path, 'rb') as f:
            fbytes = f.read()

        up_req = urllib.request.Request(
            'https://brainyogaacademy.com/wp-json/wp/v2/media',
            data=fbytes,
            headers={
                'User-Agent': 'Mozilla/5.0',
                'X-WP-Nonce': api_nonce,
                'Content-Disposition': f'attachment; filename="{fname}"',
                'Content-Type': mime
            }
        )
        try:
            with opener.open(up_req) as resp:
                up_res = json.loads(resp.read().decode('utf-8'))
                media_map[fname] = {'id': up_res['id'], 'url': up_res['source_url']}
                print(f"[UPLOADED] {fname} -> ID: {up_res['id']}, URL: {up_res['source_url']}")
        except Exception as e:
            print(f"[UPLOAD FAILED] {fname}: {e}")

with open(MEDIA_MAP_FILE, 'w') as f:
    json.dump(media_map, f, indent=2)
print("Saved wp_media_map.json with total items:", len(media_map))
