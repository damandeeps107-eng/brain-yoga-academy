import subprocess
import json

script = """
<script>
window.addEventListener('load', () => {
    const ids = [
        'header',
        'header > div',
        'header a:first-child',
        'header a:first-child img',
        'header a:first-child span',
        'nav',
        '#mobileMenuToggle',
        'header button.by-btn-primary'
    ];
    for (const sel of ids) {
        const el = document.querySelector(sel);
        if (el) {
            const r = el.getBoundingClientRect();
            console.log('MEASURE: ' + sel + ' => left=' + r.left + ' right=' + r.right + ' width=' + r.width + ' height=' + r.height + ' display=' + window.getComputedStyle(el).display);
        } else {
            console.log('NOT FOUND: ' + sel);
        }
    }
});
</script>
"""

with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html') as f:
    content = f.read()

content_with_debug = content.replace('</body>', script + '\n</body>')
with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/debug_measure.html', 'w') as f:
    f.write(content_with_debug)

cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless=new",
    "--disable-gpu",
    "--window-size=390,844",
    "--enable-logging=stderr",
    "--dump-dom",
    "file:///Users/user/.gemini/antigravity/scratch/brain-yoga-landing/debug_measure.html"
]
res = subprocess.run(cmd, capture_output=True, text=True)
for line in res.stderr.splitlines():
    if 'MEASURE:' in line or 'NOT FOUND:' in line:
        print(line)
