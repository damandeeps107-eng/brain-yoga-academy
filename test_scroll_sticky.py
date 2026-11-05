#!/usr/bin/env python3
import subprocess, time, json, urllib.request, asyncio, websockets

async def test_scroll():
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
        
        await ws.send(json.dumps({
            'id': 3,
            'method': 'Emulation.setDeviceMetricsOverride',
            'params': {'width': 390, 'height': 844, 'deviceScaleFactor': 3, 'mobile': True}
        }))
        
        await ws.send(json.dumps({'id': 4, 'method': 'Page.navigate', 'params': {'url': 'https://brainyogaacademy.com/'}}))
        await asyncio.sleep(3.0)
        
        for scroll_y in [0, 30, 80, 150, 200]:
            scroll_code = f"""
            (function() {{
                window.scrollTo(0, {scroll_y});
                var bar = document.querySelector('.elementor-element-by_top_announcement_bar');
                var mob = document.querySelector('.elementor-element-b7ec46a');
                var rBar = bar ? bar.getBoundingClientRect() : null;
                var rMob = mob ? mob.getBoundingClientRect() : null;
                var sMob = mob ? window.getComputedStyle(mob) : null;
                return {{
                    scrollY: {scroll_y},
                    barTop: rBar ? rBar.top : null,
                    barBottom: rBar ? rBar.bottom : null,
                    mobTop: rMob ? rMob.top : null,
                    mobBottom: rMob ? rMob.bottom : null,
                    mobPos: sMob ? sMob.position : null,
                    mobStyleTop: sMob ? sMob.top : null,
                    mobClasses: mob ? mob.className : null
                }};
            }})()
            """
            await ws.send(json.dumps({'id': 10 + scroll_y, 'method': 'Runtime.evaluate', 'params': {'expression': scroll_code, 'returnByValue': True}}))
            while True:
                data = json.loads(await ws.recv())
                if data.get('id') == 10 + scroll_y:
                    print(json.dumps(data.get('result', {}).get('result', {}).get('value', {})))
                    break
                    
    proc.terminate()

asyncio.run(test_scroll())
