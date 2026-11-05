import re

with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace CSS
css_old = r'\.by-brand-logo \{.*?@media \(max-width: 640px\) \{.*?\.by-brand-logo \{.*?\}\s*\}'
css_new = """.by-brand-logo {
            height: 35px !important;
            max-height: 35px !important;
            width: auto !important;
            max-width: 200px !important;
            object-fit: contain !important;
            display: block !important;
        }
        @media (max-width: 640px) {
            .by-brand-logo {
                height: 25px !important;
                max-height: 25px !important;
                max-width: 145px !important;
            }
        }"""
html = re.sub(css_old, css_new, html, flags=re.DOTALL)

# Remove inline height: 36px !important from by-brand-logo img tag so CSS media query works!
html = html.replace(
    'class="by-brand-logo" style="height: 36px !important; width: auto !important; max-width: 205px !important; object-fit: contain !important; display: block !important;"',
    'class="by-brand-logo" style="width: auto !important; object-fit: contain !important; display: block !important;"'
)

# On mobile action button, ensure concise sizing
old_btn = '<button onclick="openModal(\'individualModal\')" class="by-btn-primary !py-2 !px-2.5 sm:!px-4 !text-xs sm:!text-sm flex items-center gap-1.5 whitespace-nowrap">'
new_btn = '<button onclick="openModal(\'individualModal\')" class="by-btn-primary !py-1.5 sm:!py-2 !px-2.5 sm:!px-4 !text-[11px] sm:!text-sm flex items-center gap-1 sm:gap-1.5 whitespace-nowrap">'
html = html.replace(old_btn, new_btn)

# Hamburger button sizing
old_hamb = 'class="xl:hidden w-9 h-9 sm:w-10 sm:h-10 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-800 flex items-center justify-center transition-all flex-shrink-0"'
new_hamb = 'class="xl:hidden w-8 h-8 sm:w-9 sm:h-9 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-800 flex items-center justify-center transition-all flex-shrink-0"'
html = html.replace(old_hamb, new_hamb)

with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Tuned mobile logo and header classes!")
