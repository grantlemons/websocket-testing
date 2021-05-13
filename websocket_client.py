import asyncio
import websockets
import aioconsole

loop = asyncio.get_event_loop()
uri = "ws://localhost:8765"

user = input('Username: ')
password = input('Password: ')

async def transmit(message = ''):
    if message == '':
        message = await aioconsole.ainput('Message: ')
    async with websockets.connect(uri) as websocket:
        await websocket.send( user )
        await websocket.send( password )
        await websocket.send( message )
        
        print(f"> {message}")

async def recieve():
    async with websockets.connect(uri) as websocket:
        response = await asyncio.wait_for( websocket.recv(), timeout=1 )
        print(f"{response}")
        
async def trans_wait(message = ''):
    if message == '':
        message = await aioconsole.ainput('Message: ')
    async with websockets.connect(uri) as websocket:
        await websocket.send( user )
        await websocket.send( password )
        await websocket.send( message )
        
        #print(f"> {message}")
        
        response = await websocket.recv()
        print(f"{response}")

async def run():
    await trans_wait()
    await recieve() 
    
try:
    while True:
        loop.run_until_complete( run() )
except KeyboardInterrupt:
    pass