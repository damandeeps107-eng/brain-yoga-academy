import urllib.request
import subprocess

script = """
(() => {
    const el1 = document.querySelector('.elementor-element-by_top_announcement_bar');
    const el2 = document.querySelector('.elementor-element-52259ba');
    const el3 = document.querySelector('.elementor-element-b7ec46a');
    console.log('BAR:', el1 ? window.getComputedStyle(el1).display : 'null');
    console.log('DESKTOP_HDR:', el2 ? window.getComputedStyle(el2).display : 'null');
    console.log('MOBILE_HDR:', el3 ? window.getComputedStyle(el3).display : 'null');
})();
"""

# Let's run chrome with virtual-time-budget or screenshot
cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless=new",
    "--disable-gpu",
    "--window-size=1280,800",
    "--enable-logging=stderr",
    "--run-all-compositor-stages-before-draw",
    "https://brainyogaacademy.com/"
]
