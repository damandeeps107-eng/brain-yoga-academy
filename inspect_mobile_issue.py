#!/usr/bin/env python3
import subprocess, time, json, urllib.request, asyncio, websockets

async def inspect_mobile_header():
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
            'params': {
                'width': 390,
                'height': 844,
                'deviceScaleFactor': 3,
                'mobile': True
            }
        }))
        
        await ws.send(json.dumps({'id': 4, 'method': 'Page.navigate', 'params': {'url': 'https://brainyogaacademy.com/'}}))
        await asyncio.sleep(3.0)
        
        eval_script = """
        (function() {
            var bar = document.getElementById('by_top_announcement_bar');
            var mobileHeader = document.querySelector('.elementor-element-b7ec46a');
            var desktopHeader = document.querySelector('.elementor-element-52259ba');
            var headerContainer = document.querySelector('header') || document.querySelector('.elementor-location-header');
            
            function getInfo(el, name) {
                if (!el) return name + ': NOT FOUND';
                var r = el.getBoundingClientRect();
                var s = window.getComputedStyle(el);
                return name + ': rect[top=' + r.top + ', left=' + r.left + ', width=' + r.width + ', height=' + r.height + ']' +
                       ' | pos=' + s.position + ' top=' + s.top + ' zIndex=' + s.zIndex + ' display=' + s.display +
                       ' margin=' + s.marginTop + ' ' + s.marginRight + ' ' + s.marginBottom + ' ' + s.marginLeft;
            }
            
            return {
                bar: getInfo(bar, 'TopBar'),
                mobileHeader: getInfo(mobileHeader, 'MobileHeader_b7ec46a'),
                desktopHeader: getInfo(desktopHeader, 'DesktopHeader_52259ba'),
                headerContainer: getInfo(headerContainer, 'HeaderParent'),
                htmlScrollY: window.scrollY
            };
        })()
        """
        
        await ws.send(json.dumps({'id': 5, 'method': 'Runtime.evaluate', 'params': {'expression': eval_script, 'returnByValue': True}}))
        
        resp = await ws.recv()
        while True:
            data = json.loads(resp)
            if data.get('id') == 5:
                print(json.dumps(data.get('result', {}).get('result', {}).get('value', {}), indent=2))
                break
            resp = await ws.recv()
            
        # Take a screenshot of the top 300px
        await ws.send(json.dumps({
            'id': 6,
            'method': 'Page.captureScreenshot',
            'params': {'clip': {'x': 0, 'y': 0, 'width': 390, 'height': 500, 'scale': 2}}
        }))
        while True:
            data = json.loads(await ws.recv())
            if data.get('id') == 6:
                import base64
                img_data = base64.b64decode(data['result']['data'])
                with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/mobile_top_screenshot.png', 'wb') as f:
                    f.write(img_data)
                print("Screenshot saved to mobile_top_screenshot.png")
                break
                
    proc.terminate()

asyncio.run(inspect_mobile_header())
