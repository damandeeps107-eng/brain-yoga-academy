#!/usr/bin/env python3
import subprocess, time, json, urllib.request, asyncio, websockets

async def check_css():
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
        
        script = """
        (function() {
            var header = document.querySelector('header');
            var bar = document.querySelector('.elementor-element-by_top_announcement_bar');
            var mob = document.querySelector('.elementor-element-b7ec46a');
            var hero = document.querySelector('main') || document.querySelector('.elementor-location-single') || document.querySelector('article');
            
            function dump(el, name) {
                if (!el) return name + ': NOT FOUND';
                var r = el.getBoundingClientRect();
                var s = window.getComputedStyle(el);
                return {
                    name: name,
                    rect: {top: r.top, bottom: r.bottom, height: r.height, width: r.width},
                    style: {
                        position: s.position,
                        top: s.top,
                        marginTop: s.marginTop,
                        marginBottom: s.marginBottom,
                        paddingTop: s.paddingTop,
                        paddingBottom: s.paddingBottom,
                        zIndex: s.zIndex
                    }
                };
            }
            
            return {
                header: dump(header, 'header'),
                bar: dump(bar, 'announcement_bar'),
                mob: dump(mob, 'mobile_header'),
                hero: dump(hero, 'hero_parent')
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

asyncio.run(check_css())
