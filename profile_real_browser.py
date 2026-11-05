#!/usr/bin/env python3
import subprocess, time, json, urllib.request, asyncio, websockets

async def profile_url(url):
    print(f"\n==========================================")
    print(f"PROFILING: {url}")
    print(f"==========================================")
    
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
        # Enable network and page
        await ws.send(json.dumps({'id': 1, 'method': 'Network.enable'}))
        await ws.send(json.dumps({'id': 2, 'method': 'Page.enable'}))
        await ws.send(json.dumps({'id': 3, 'method': 'Performance.enable'}))
        
        requests = {}
        slow_requests = []
        
        t0 = time.time()
        await ws.send(json.dumps({'id': 4, 'method': 'Page.navigate', 'params': {'url': url}}))
        
        load_time = None
        dcl_time = None
        
        start_time = time.time()
        while time.time() - start_time < 12:
            try:
                msg = await asyncio.wait_for(ws.recv(), timeout=1.5)
                data = json.loads(msg)
                method = data.get('method', '')
                
                if method == 'Network.requestWillBeSent':
                    req_id = data['params']['requestId']
                    req_url = data['params']['request']['url']
                    requests[req_id] = {'url': req_url, 'start': time.time()}
                    
                elif method == 'Network.loadingFinished':
                    req_id = data['params']['requestId']
                    if req_id in requests:
                        dur = time.time() - requests[req_id]['start']
                        requests[req_id]['dur'] = dur
                        if dur > 0.4:
                            slow_requests.append((dur, requests[req_id]['url']))
                            
                elif method == 'Page.domContentEventFired':
                    dcl_time = time.time() - t0
                    print(f"  ⚡ DOMContentLoaded: {dcl_time:.2f}s")
                    
                elif method == 'Page.loadEventFired':
                    load_time = time.time() - t0
                    print(f"  🏁 Page Load Event: {load_time:.2f}s")
                    break
            except asyncio.TimeoutError:
                break
                
        print(f"\nSlow resources (> 400ms):")
        for dur, rurl in sorted(slow_requests, reverse=True)[:10]:
            print(f"  {dur:.2f}s: {rurl[:90]}")
            
    proc.terminate()

async def main():
    await profile_url('https://brainyogaacademy.com/')
    await profile_url('https://brainyogaacademy.com/brain-yoga-for-busy-minds/')

asyncio.run(main())
