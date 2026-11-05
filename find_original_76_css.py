with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/home_raw.html') as f:
    html = f.read()

import re
# Find all CSS in home_raw.html referencing elementor-76
styles = re.findall(r'<style[^>]*id=[\'"]elementor-post-76-css[\'"][^>]*>(.*?)</style>', html, re.DOTALL)
if styles:
    print('Found elementor-post-76-css in home_raw.html! Length:', len(styles[0]))
    with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/original_header_76.css', 'w') as out:
        out.write(styles[0])
else:
    # search for post-76 css link
    links = re.findall(r'href=[\'"]([^\'"]*post-76\.css[^\'"]*)[\'"]', html)
    print('Links to post-76.css:', links)
