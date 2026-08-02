import asyncio
import websockets
import threading
import time
import json

ER = '\33[91m'
RS = '\33[0m'
CY = '\33[0;36m'
GR = '\33[0;32m'

class Client():
    def __init__(self):
        self.wsock = None
        self.active = False
        #async
        self._loop = asyncio.new_event_loop()
        self._thread = None
        self._stop_event = None

    def push(self,name:str,link:str=None,action:str=None,title:str=None,subtitle:str=None,imgSrc:str=None,startedAt:int=None,endsAt:int=None):
        if not self.active:
            print(f"{ER}[Client] Connection to nerimity must to be active to push presence.{RS}")
            return

        data = {
            "name": name,
            "link": link,
            "action": action,
            "title": title,
            "subtitle": subtitle,
            "imgSrc": imgSrc,
            "startedAt": startedAt,
            "endsAt": endsAt
        }

        clean_payload = {key: str(value) for key, value in data.items() if value is not None}
        joined = {
            "name": 'UPDATE_RPC',
            "data": clean_payload
            }
        json_step = json.dumps(joined)

        asyncio.run_coroutine_threadsafe(self._push(json_step),self._loop)

    def close(self):
        if not self.active or self._stop_event.is_set():
            print(f"{ER}[Client] Connection to nerimity must to be active to close.{RS}")
            return
        
        asyncio.run_coroutine_threadsafe(self._close(),self._loop)
    
    def start(self):
        if self.active:
            print(f"{ER}[Client] Can't start an active client.{RS}")
            return
        self._thread = threading.Thread(target=self._start, daemon=True)
        self._thread.start()
        
        print(f"{CY}[Client] Starting{RS}")
        while not self.active and self._thread.is_alive():
            time.sleep(0.1)

    def _start(self):
        asyncio.set_event_loop(self._loop)
        self._loop.run_until_complete(self._websocket_connection())

    async def _push(self, data):
        try:
            await self.wsock.send(data)
        except Exception as e:
            print(f"{ER}[Client] Err while pushing data: {e}{RS}")

    async def _close(self):
        if self._stop_event:
            print(f"{GR}[Client] Connection with nerimity closed{RS}")
            self._stop_event.set()

    async def _websocket_connection(self):
        self._stop_event = asyncio.Event()
        print(f"{CY}[Client] Trying to establish a websocket connection{RS}")
        for port in range(6463, 6473):
            url = f"ws://localhost:{port}/?appId=123455678987654321"
            try:
                async with websockets.connect(url) as ws:
                    #print(f"[Client] Trying port:{port}")
                    a = await ws.recv()
                    if not a == '{"name":"HELLO_NERIMITY_RPC"}' :
                        continue
                    await ws.send('{"name":"HELLO_NERIMITY_RPC"}')
                    self.wsock = ws
                    print(f"{GR}[Client] Websocket connection to nerimity active{RS}")
                    self.active = True
                    await self._stop_event.wait()
                    print(f"{GR}[Client] Websocket connection to nerimity closed{RS}")
                    self.active = False
                    return
            except asyncio.CancelledError:
                print(f"{ER}[Client] Asyncio.CancelledError in Client websocket - connection force closed?{RS}")
                ws.close()
                raise
            except ConnectionError:
                pass

            except Exception as e:
                print(e)
                return
        print(f"{ER}[Client] Couldn't connect to nerimity: No port responded. - Nerimity open?{RS}")
