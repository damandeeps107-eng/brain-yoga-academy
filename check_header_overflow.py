#!/usr/bin/env python3
import subprocess, time, json, urllib.request, asyncio, websockets

async def inspect_desktop_header():
    cmd = [
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '--headless=new',
        '--disable-gpu',
        '--window-size=1728,1117',
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
        
        await ws.send(json.dumps({'id': 4, 'method': 'Page.navigate', 'params': {'url': 'https://brainyogaacademy.com/brain-yoga-for-busy-minds/'}}))
        await asyncio.sleep(2.5)
        
        script = """
        (function() {
            var header = document.querySelector('header');
            var container = header ? header.querySelector('div') : null;
            var logo = header ? header.querySelector('a') : null;
            var nav = header ? header.querySelector('nav') : null;
            var ctaDiv = header ? header.querySelector('div.flex-shrink-0, div:last-child') : null;
            var btn = header ? header.querySelector('button.by-btn-primary') : null;
            
            function b(el, name) {
                if (!el) return name + ': null';
                var r = el.getBoundingClientRect();
                return name + ': left=' + r.left.toFixed(0) + ' right=' + r.right.toFixed(0) + ' w=' + r.width.toFixed(0) + ' (window.w=' + window.innerWidth + ')';
            }
            
            return {
                windowWidth: window.innerWidth,
                header: b(header, 'Header'),
                container: b(container, 'Container'),
                logo: b(logo, 'Logo'),
                nav: b(nav, 'Nav'),
                btn: b(btn, 'Btn'),
                isBtnOverflowing: btn ? (btn.getBoundingClientRect().right > window.innerWidth) : false,
                overflowDistance: btn ? (btn.getBoundingClientRect().right - window.innerWidth) : 0
            };
        })()
        """
        await ws.send(json.dumps({'id': 5, 'method': 'Runtime.evaluate', 'params': {'expression': script, 'returnByValue': True}}))
        
        while True:
            data = json.loads(await ws.recv())
            if data.get('id') == 5:
                print(json.dumps(data.get('result', {}).get('result', {}).get('value', {}), indent=2))
                break
                
    proc.terminate()

asyncio.run(inspect_desktop_header())
