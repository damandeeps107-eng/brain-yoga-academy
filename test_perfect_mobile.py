#!/usr/bin/env python3
"""
Test the exact visual fix in headless Chrome:
1. Make by_top_announcement_bar sleek and compact on mobile (36px).
2. Set hero margin-top so it pulls up under b7ec46a without any white gap.
3. Capture screenshot to verify.
"""
import subprocess, time, json, urllib.request, asyncio, websockets, base64

async def test_perfect_mobile():
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
        
        inject_code = """
        (function() {
            var s = document.createElement('style');
            s.id = 'by-perfect-mobile-fix';
            s.textContent = `
                /* Compact sleek announcement bar on all screens */
                .elementor-element-by_top_announcement_bar {
                    padding: 6px 12px !important;
                    background-color: #007984 !important;
                    position: relative !important;
                    z-index: 99 !important;
                }
                
                @media (max-width: 767px) {
                    /* On mobile: compact single-line layout */
                    .elementor-element-by_top_announcement_bar .by-flicker-btn {
                        font-size: 11px !important;
                        padding: 3px 10px !important;
                    }
                    .elementor-element-by_top_announcement_html .by-subtitle {
                        display: none !important;
                    }
                    .elementor-element-by_top_announcement_bar > div > div {
                        gap: 6px !important;
                    }
                    /* Ensure mobile header sits naturally and hero pulls up under it */
                    .elementor-element-b7ec46a {
                        margin-top: 0 !important;
                        position: relative !important;
                    }
                    .elementor-element-41455f9 {
                        margin-top: -68px !important; /* Pull hero under the 68px transparent navbar */
                    }
                }
                
                @media (min-width: 768px) {
                    .elementor-element-41455f9 {
                        margin-top: -90px !important;
                    }
                }
            `;
            document.head.appendChild(s);
            
            // Mark subtitle for hiding on mobile
            var spans = document.querySelectorAll('.elementor-element-by_top_announcement_html span');
            spans.forEach(function(sp) {
                if (sp.textContent.includes('Working professionals')) {
                    sp.classList.add('by-subtitle');
                }
            });
            
            return 'injected';
        })()
        """
        await ws.send(json.dumps({'id': 5, 'method': 'Runtime.evaluate', 'params': {'expression': inject_code, 'returnByValue': True}}))
        
        while True:
            data = json.loads(await ws.recv())
            if data.get('id') == 5:
                print('Injected fix successfully')
                break
                
        await asyncio.sleep(1.0)
        
        # Take screenshot of mobile view with fix applied
        await ws.send(json.dumps({
            'id': 6,
            'method': 'Page.captureScreenshot',
            'params': {'format': 'png'}
        }))
        while True:
            data = json.loads(await ws.recv())
            if data.get('id') == 6:
                img_data = base64.b64decode(data['result']['data'])
                with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/mobile_verified_fix.png', 'wb') as f:
                    f.write(img_data)
                print("Screenshot saved to mobile_verified_fix.png")
                break
                
    proc.terminate()

asyncio.run(test_perfect_mobile())
