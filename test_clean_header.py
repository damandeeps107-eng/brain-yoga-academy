#!/usr/bin/env python3
"""
Test the exact clean header fix:
- Teal compact bar at top (34px)
- Crisp mobile navbar
- Hero margin-top: 0 with clean padding
"""
import subprocess, time, json, urllib.request, asyncio, websockets, base64

async def test_clean_mobile():
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
        
        fix_css = """
        (function() {
            var s = document.createElement('style');
            s.id = 'by-clean-header-fix';
            s.textContent = `
                @media (max-width: 767px) {
                    .elementor-element-by_top_announcement_bar {
                        padding: 7px 10px !important;
                        background: #007984 !important;
                    }
                    .by-hide-on-mobile {
                        display: none !important;
                    }
                    .by-flicker-btn {
                        font-size: 11px !important;
                        padding: 3px 12px !important;
                    }
                    .elementor-element-b7ec46a {
                        background-color: #1a2730 !important;
                        padding: 10px 14px !important;
                        margin: 0 !important;
                        position: relative !important;
                    }
                    .elementor-1111 .elementor-element-41455f9 {
                        margin-top: 0 !important;
                        padding-top: 15px !important;
                    }
                }
            `;
            document.head.appendChild(fix_css);
            
            // Mark elements to hide on mobile
            var spans = document.querySelectorAll('.elementor-element-by_top_announcement_html span');
            spans.forEach(function(sp) {
                if (sp.textContent.includes('Working professionals') || sp.textContent.includes('Adult Wellness')) {
                    sp.classList.add('by-hide-on-mobile');
                }
            });
            return 'done';
        })()
        """
        await ws.send(json.dumps({'id': 5, 'method': 'Runtime.evaluate', 'params': {'expression': fix_css, 'returnByValue': True}}))
        
        while True:
            data = json.loads(await ws.recv())
            if data.get('id') == 5:
                print('Fix applied in DOM')
                break
                
        await asyncio.sleep(0.5)
        
        # Capture screenshot
        await ws.send(json.dumps({
            'id': 6,
            'method': 'Page.captureScreenshot',
            'params': {'format': 'png'}
        }))
        while True:
            data = json.loads(await ws.recv())
            if data.get('id') == 6:
                img_data = base64.b64decode(data['result']['data'])
                with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/mobile_clean_result.png', 'wb') as f:
                    f.write(img_data)
                print("Screenshot saved to mobile_clean_result.png")
                break
                
    proc.terminate()

asyncio.run(test_clean_mobile())
