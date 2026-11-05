import asyncio
import json
import urllib.request
import subprocess
import time
import base64
import websockets
from PIL import Image

async def capture_mobile(url, out_path):
    port = 9222
    proc = subprocess.Popen([
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "--headless=new",
        f"--remote-debugging-port={port}",
        "--disable-gpu"
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1.5)

    try:
        # Get list of targets
        req = urllib.request.urlopen(f"http://127.0.0.1:{port}/json/list")
        tabs = json.loads(req.read().decode('utf-8'))
        ws_url = tabs[0]['webSocketDebuggerUrl']

        async with websockets.connect(ws_url) as ws:
            msg_id = 1
            async def send(method, params=None):
                nonlocal msg_id
                cmd = {"id": msg_id, "method": method, "params": params or {}}
                msg_id += 1
                await ws.send(json.dumps(cmd))
                while True:
                    res = json.loads(await ws.recv())
                    if res.get("id") == cmd["id"]:
                        return res.get("result", {})

            await send("Page.enable")
            # Set genuine mobile viewport 390x844
            await send("Emulation.setDeviceMetricsOverride", {
                "width": 390,
                "height": 844,
                "deviceScaleFactor": 1,
                "mobile": True
            })
            await send("Emulation.setUserAgentOverride", {
                "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"
            })
            # Navigate to url
            await send("Page.navigate", {"url": url})
            # Wait 2 seconds for render
            await asyncio.sleep(2.5)

            # Capture screenshot
            res = await send("Page.captureScreenshot", {"format": "png"})
            img_data = base64.b64decode(res["data"])
            with open(out_path, "wb") as f:
                f.write(img_data)
            print("Successfully captured genuine mobile screenshot:", out_path)
    finally:
        proc.terminate()

asyncio.run(capture_mobile(
    "file:///Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html",
    "/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/true_mobile_390.png"
))

# Crop top 220px to inspect header
im = Image.open("/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/true_mobile_390.png")
im.crop((0, 0, im.width, 180)).save("/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/true_mobile_header_crop.png")
print("Cropped header saved!")
