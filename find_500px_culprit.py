import subprocess

script = """
<script>
window.addEventListener('load', () => {
    // Temporarily hide sections one by one to find which one causes body width to be 500px
    const children = Array.from(document.body.children);
    for (const ch of children) {
        if (ch.tagName === 'SCRIPT' || ch.tagName === 'STYLE') continue;
        const prevDisplay = ch.style.display;
        ch.style.display = 'none';
        const w = document.body.offsetWidth;
        ch.style.display = prevDisplay;
        console.log('HIDE ' + ch.tagName + (ch.id ? '#'+ch.id : '') + ' => body width becomes ' + w);
    }
});
</script>
"""

with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html') as f:
    content = f.read()

content_with_debug = content.replace('</body>', script + '\n</body>')
with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/debug_culprit.html', 'w') as f:
    f.write(content_with_debug)

cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless=new",
    "--disable-gpu",
    "--window-size=390,844",
    "--enable-logging=stderr",
    "--dump-dom",
    "file:///Users/user/.gemini/antigravity/scratch/brain-yoga-landing/debug_culprit.html"
]
res = subprocess.run(cmd, capture_output=True, text=True)
for line in res.stderr.splitlines():
    if 'HIDE ' in line:
        print(line)
