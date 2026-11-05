import subprocess
from PIL import Image

resolutions = [
    (1440, 900, "live_1440"),
    (1280, 800, "live_1280"),
    (1024, 768, "live_1024"),
    (500, 844, "live_500")
]

for w, h, name in resolutions:
    cmd = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "--headless",
        "--disable-gpu",
        f"--window-size={w},{h}",
        f"--screenshot=/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/{name}.png",
        "https://brainyogaacademy.com/brain-yoga-for-busy-minds/?v=nocache_final"
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    im = Image.open(f"/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/{name}.png")
    im.crop((0, 0, im.width, 160)).save(f"/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/crop_{name}.png")
    print(f"Captured {name} ({w}px)")
