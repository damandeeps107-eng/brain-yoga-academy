import subprocess
import json

script = """
<script>
window.addEventListener('load', () => {
    const docWidth = document.documentElement.offsetWidth;
    console.log('DOC_WIDTH: ' + docWidth + ' BODY_WIDTH: ' + document.body.offsetWidth);
    const elements = document.querySelectorAll('*');
    for (const el of elements) {
        const rect = el.getBoundingClientRect();
        if (rect.right > 390) {
            console.log('OVERFLOW: ' + el.tagName + '.' + el.className + ' right=' + rect.right + ' width=' + rect.width);
        }
    }
});
</script>
"""

with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html') as f:
    content = f.read()

# Add script before </body>
content_with_debug = content.replace('</body>', script + '\n</body>')
with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/debug_overflow.html', 'w') as f:
    f.write(content_with_debug)

# Run chrome headless with --enable-logging=stderr
cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    "--window-size=390,844",
    "--enable-logging=stderr",
    "--screenshot=/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/debug_390.png",
    "file:///Users/user/.gemini/antigravity/scratch/brain-yoga-landing/debug_overflow.html"
]
res = subprocess.run(cmd, capture_output=True, text=True)
for line in res.stderr.splitlines():
    if 'OVERFLOW:' in line or 'DOC_WIDTH:' in line:
        print(line)
