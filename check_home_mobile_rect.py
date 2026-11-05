import subprocess

cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless=new",
    "--disable-gpu",
    "--window-size=500,844",
    "--enable-logging=stderr",
    "--dump-dom",
    "https://brainyogaacademy.com/"
]
res = subprocess.run(cmd, capture_output=True, text=True)
# check if b7ec46a is in dom
print("Has b7ec46a:", "b7ec46a" in res.stdout)
print("Has by_top_announcement_bar:", "by_top_announcement_bar" in res.stdout)
