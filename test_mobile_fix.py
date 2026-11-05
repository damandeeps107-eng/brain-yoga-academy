#!/usr/bin/env python3
"""
Test different margin-top and compact bar on mobile 390px in headless Chrome.
"""
import subprocess, time, json, urllib.request, asyncio, websockets, base64

async def test_compact_mobile():
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
        
        # Mobile viewport 390x844
        await ws.send(json.dumps({
            'id': 3,
            'method': 'Emulation.setDeviceMetricsOverride',
            'params': {'width': 390, 'height': 844, 'deviceScaleFactor': 3, 'mobile': True}
        }))
        
        await ws.send(json.dumps({'id': 4, 'method': 'Page.navigate', 'params': {'url': 'https://brainyogaacademy.com/'}}))
        await asyncio.sleep(2.5)
        
        # Inject the CSS fix directly in the browser to test
        inject_css = """
        (function() {
            var s = document.createElement('style');
            s.id = 'by-test-fix';
            s.textContent = `
                @media (max-width: 767px) {
                    /* Sleek compact bar */
                    .elementor-element-by_top_announcement_bar {
                        padding: 6px 8px !important;
                    }
                    .by-mobile-hide {
                        display: none !important;
                    }
                    /* Pull hero section up so transparent header seamlessly overlays the boy image without white gap */
                    .elementor-element-41455f9 {
                        margin-top: -108px !important;
                    }
                }
            `;
            document.head.appendChild(s);
            
            // Hide the long subtitle on mobile
            var text = document.querySelector('#by-top-announcement-text');
            if (text) text.classList.add('by-mobile-hide');
            
            var mob = document.querySelector('.elementor-element-b7ec46a');
            var hero = document.querySelector('.elementor-element-41455f9');
            var rMob = mob ? mob.getBoundingClientRect() : null;
            var rHero = hero ? hero.getBoundingClientRect() : null;
            return {
                mobBottom: rMob ? rMob.bottom : null,
                heroTop: rHero ? rHero.top : null,
                gap: (rHero && rMob) ? (rHero.top - rMob.bottom) : null
            };
        })()
        """
        await ws.send(json.dumps({'id': 5, 'method': 'Runtime.evaluate', 'params': {'expression': inject_css, 'returnByValue': True}}))
        
        while True:
            data = json.loads(await ws.recv())
            if data.get('id') == 5:
                print('Fix evaluation result:', json.dumps(data.get('result', {}).get('result', {}).get('value', {}), indent=2))
                break
                
        # Capture screenshot
        await ws.send(json.dumps({
            'id': 6,
            'method': 'Page.captureScreenshot',
            'params': {'clip': {'x': 0, 'y': 0, 'width': 390, 'height': 600, 'scale': 2}}
        }))
        while True:
            data = json.loads(await ws.recv())
            if data.get('id') == 6:
                img_data = base64.b64decode(data['result']['data'])
                with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/mobile_fixed_screenshot.png', 'wb') as f:
                    f.write(img_data)
                print("Screenshot saved to mobile_fixed_screenshot.png")
                break
                
    proc.terminate()

asyncio.run(test_compact_mobile())
