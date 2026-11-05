import subprocess
from PIL import Image

cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless=new",
    "--disable-gpu",
    "--window-size=390,844",
    "--screenshot=/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/test_new_390.png",
    "file:///Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html"
]
subprocess.run(cmd, check=True)
im = Image.open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/test_new_390.png')
print("Image size with --headless=new:", im.size)
im.crop((0, 0, im.width, 160)).save('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/crop_new_390.png')
