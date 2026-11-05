import json, re

# Read busy-minds.html
with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix header logo with bulletproof inline styles
old_header_logo = re.search(r'<a href=[\'"]busy-minds\.html[\'"][^>]*class=[\'"][^\'"]*group[^\'"]*[\'"][^>]*>.*?</a>', html, re.DOTALL)
if old_header_logo:
    print("Found header logo block:")
    print(old_header_logo.group(0))

new_header_logo = '''<a href="https://brainyogaacademy.com/brain-yoga-for-busy-minds/" style="display: flex !important; align-items: center !important; gap: 10px !important; text-decoration: none !important; flex-shrink: 0 !important; max-width: 280px !important;">
                <img decoding="async" src="https://brainyogaacademy.com/wp-content/uploads/2026/11/official_logo.png" alt="Brain Yoga Academy" style="height: 38px !important; max-height: 38px !important; width: auto !important; max-width: 210px !important; object-fit: contain !important; display: block !important;">
                <span style="display: inline-block !important; font-size: 10px !important; font-weight: 700 !important; text-transform: uppercase !important; letter-spacing: 0.08em !important; background: #D2F0FF !important; color: #007984 !important; border: 1px solid rgba(0,121,132,0.2) !important; padding: 3px 8px !important; border-radius: 6px !important; white-space: nowrap !important;">
                    For Busy Minds
                </span>
            </a>'''

if old_header_logo:
    html = html.replace(old_header_logo.group(0), new_header_logo)

# Also fix footer logo
old_footer_logo = re.search(r'<a href=[\'"]#[\'"][^>]*class=[\'"]inline-flex items-center gap-2[\'"][^>]*>\s*<img src=[\'"]official_logo\.png[\'"][^>]*>\s*</a>', html)
if old_footer_logo:
    new_footer_logo = '''<a href="https://brainyogaacademy.com/brain-yoga-for-busy-minds/" style="display: inline-flex !important; align-items: center !important; gap: 8px !important;">
                        <img decoding="async" src="https://brainyogaacademy.com/wp-content/uploads/2026/11/official_logo.png" alt="Brain Yoga Academy" style="height: 42px !important; max-height: 42px !important; width: auto !important; max-width: 230px !important; object-fit: contain !important; display: inline-block !important;">
                    </a>'''
    html = html.replace(old_footer_logo.group(0), new_footer_logo)

# Add explicit CSS rule in <style> to prevent any theme override
header_css_fix = """
        /* Bulletproof Header & Logo Constraints across all browsers */
        header {
            position: sticky !important;
            top: 0 !important;
            z-index: 99999 !important;
            background-color: rgba(255, 255, 255, 0.98) !important;
            backdrop-filter: blur(8px) !important;
            border-bottom: 1px solid #E2E8F0 !important;
            width: 100% !important;
            max-width: 100vw !important;
        }
        header img, header a img {
            height: 38px !important;
            max-height: 38px !important;
            width: auto !important;
            max-width: 210px !important;
            object-fit: contain !important;
            display: block !important;
        }
        footer img, footer a img {
            height: 42px !important;
            max-height: 42px !important;
            width: auto !important;
            max-width: 230px !important;
            object-fit: contain !important;
            display: inline-block !important;
        }
"""

html = html.replace("/* Exact Typography Matching Children Brain Yoga (kids.html) */", header_css_fix + "\n        /* Exact Typography Matching Children Brain Yoga (kids.html) */")

with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated busy-minds.html with bulletproof logo constraints!")
