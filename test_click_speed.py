#!/usr/bin/env python3
import subprocess, time, json, urllib.request, asyncio, websockets

async def test_navigation():
    cmd = [
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '--headless=new',
        '--disable-gpu',
        '--remote-debugging-port=9222',
        'about:blank'
    ]
    proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    await asyncio.sleep(1.2)
    
    tabs = json.loads(urllib.request.urlopen('http://localhost:9222/json').read())
    ws_url = tabs[0]['webSocketDebuggerUrl']
    
    async with websockets.connect(ws_url) as ws:
        await ws.send(json.dumps({'id': 1, 'method': 'Page.enable'}))
        await ws.send(json.dumps({'id': 2, 'method': 'Runtime.enable'}))
        
        print("Navigating to Homepage...")
        t0 = time.time()
        await ws.send(json.dumps({'id': 3, 'method': 'Page.navigate', 'params': {'url': 'https://brainyogaacademy.com/'}}))
        
        # Wait 3 seconds for page and preloader to run
        await asyncio.sleep(3.0)
        print(f"Homepage settled after 3s")
        
        # Now simulate click on the Adult link!
        print("\nClicking on 'Brain Yoga for Adults'...")
        click_t0 = time.time()
        eval_click = """
        (function() {
            var a = document.querySelector('a[href*=\"brain-yoga-for-busy-minds\"]');
            if (a) { a.click(); return 'clicked'; }
            return 'not found';
        })()
        """
        await ws.send(json.dumps({'id': 4, 'method': 'Runtime.evaluate', 'params': {'expression': eval_click, 'returnByValue': True}}))
        
        # Monitor when new page is loaded
        while time.time() - click_t0 < 10:
            msg = await ws.recv()
            data = json.loads(msg)
            if data.get('method') == 'Page.loadEventFired':
                dur = time.time() - click_t0
                print(f"🏁 ADULT PAGE FULLY LOADED AFTER CLICK IN: {dur:.2f} seconds!")
                break
                
    proc.terminate()

asyncio.run(test_navigation())
