import subprocess

script = """
<script>
window.addEventListener('load', () => {
    let widest = null;
    let maxScroll = 0;
    const all = document.querySelectorAll('*');
    for (const el of all) {
        if (el.scrollWidth > 390 && el.parentElement && el.parentElement.scrollWidth <= el.scrollWidth) {
            console.log('WIDE_EL: ' + el.tagName + (el.id ? '#'+el.id : '') + ' (' + el.className + ') scrollWidth=' + el.scrollWidth + ' clientWidth=' + el.clientWidth);
        }
    }
});
</script>
"""

with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html') as f:
    content = f.read()

content_with_debug = content.replace('</body>', script + '\n</body>')
with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/debug_widest.html', 'w') as f:
    f.write(content_with_debug)

cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    "--window-size=390,844",
    "--enable-logging=stderr",
    "file:///Users/user/.gemini/antigravity/scratch/brain-yoga-landing/debug_widest.html"
]
res = subprocess.run(cmd, capture_output=True, text=True)
for line in res.stderr.splitlines():
    if 'WIDE_EL:' in line:
        print(line)
