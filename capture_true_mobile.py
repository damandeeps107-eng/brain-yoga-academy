import subprocess
import json
import time
import base64
import os
import urllib.request

# Start chrome with remote debugging
port = 9222
chrome_proc = subprocess.Popen([
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless=new",
    "--remote-debugging-port=" + str(port),
    "--disable-gpu"
])

time.sleep(1.5)

try:
    # Get webSocketDebuggerUrl
    res = urllib.request.urlopen(f"http://127.0.0.1:{port}/json/version").read()
    data = json.loads(res.decode('utf-8'))
    ws_url = data['webSocketDebuggerUrl']
    print("Chrome started, version:", data.get('Browser'))
finally:
    chrome_proc.terminate()
