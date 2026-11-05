#!/usr/bin/env python3
import subprocess, time, json, urllib.request, asyncio, websockets

async def inspect_dom_structure():
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
        
        # Set mobile viewport 390x844
        await ws.send(json.dumps({
            'id': 3,
            'method': 'Emulation.setDeviceMetricsOverride',
            'params': {'width': 390, 'height': 844, 'deviceScaleFactor': 3, 'mobile': True}
        }))
        
        await ws.send(json.dumps({'id': 4, 'method': 'Page.navigate', 'params': {'url': 'https://brainyogaacademy.com/'}}))
        await asyncio.sleep(3.0)
        
        eval_script = """
        (function() {
            var bodyChildren = [];
            var header = document.querySelector('header');
            if (header) {
                var c = header.children;
                for (var i = 0; i < c.length; i++) {
                    var el = c[i];
                    var r = el.getBoundingClientRect();
                    var s = window.getComputedStyle(el);
                    bodyChildren.push({
                        tag: el.tagName,
                        id: el.id,
                        classes: el.className,
                        rect: {top: r.top, bottom: r.bottom, height: r.height, width: r.width},
                        bg: s.backgroundColor,
                        pos: s.position,
                        display: s.display
                    });
                }
            }
            
            // Check first section of page
            var main = document.querySelector('.elementor-location-single') || document.querySelector('main');
            var firstSection = main ? main.querySelector('.elementor-section, .e-con') : null;
            var rSec = firstSection ? firstSection.getBoundingClientRect() : null;
            var sSec = firstSection ? window.getComputedStyle(firstSection) : null;
            
            return {
                headerChildren: bodyChildren,
                firstSection: {
                    tag: firstSection ? firstSection.tagName : null,
                    classes: firstSection ? firstSection.className : null,
                    rect: rSec ? {top: rSec.top, bottom: rSec.bottom, height: rSec.height} : null,
                    margin: sSec ? sSec.margin : null,
                    padding: sSec ? sSec.padding : null
                }
            };
        })()
        """
        
        await ws.send(json.dumps({'id': 5, 'method': 'Runtime.evaluate', 'params': {'expression': eval_script, 'returnByValue': True}}))
        
        while True:
            data = json.loads(await ws.recv())
            if data.get('id') == 5:
                print(json.dumps(data.get('result', {}).get('result', {}).get('value', {}), indent=2))
                break
                
    proc.terminate()

asyncio.run(inspect_dom_structure())
