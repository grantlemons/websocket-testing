import asyncio
import websockets

loop = asyncio.get_event_loop()

users = [
    {
        'username': 'GLemons',
        'password': 'tensei'
    },
    {
        'username': 'Solidyl',
        'password': 'minecraft'
    },
    {
        'username': 'NotALime',
        'password': 'bob'
    }
]

async def send_and_recieve(websocket, path):
    await recieve( websocket, path )
    #await transmit( 'cool', websocket, path )

async def recieve(websocket, path):
    try:
        username = await websocket.recv()
        password = await websocket.recv()
        message = await websocket.recv()
        
        verified = False
        for i in users:
            if username == i['username']:
                if password == i['password']:
                    print(f'Verified {username}')
                    verified = True
        if verified == False:
            print(f'Invalid Username or Password, Attempt User:{username} and Pass:{password}')
            await transmit(f'Invalid Username or Password', websocket, path)
        else:
            print(f'< {username}: {message}')
            await transmit(f'{username}: {message}', websocket, path)
    except:
        pass

async def transmit(message, websocket, path):
    await websocket.send(message)
    print(f'> {message}')

server = websockets.serve(send_and_recieve, 'localhost', 8765)

try:
    loop.run_until_complete( server )
    loop.run_forever()
except KeyboardInterrupt:
    pass