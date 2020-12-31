import serial
import asyncio
import websockets




async def da_server(websocket, path):

    ser = serial.Serial(timeout=10)
    ser.baudrate = 19200
    ser.port = 'COM1'

    ser.open()
    while True:
        print("test")
        msg = ser.readline()
        message = {}
        if(msg is not None):
            message = json.dumps(msg)

        if(bool(message)):
            #print(json.dumps(message))
            await websocket.send(json.dumps(message))
        await asyncio.sleep(1)
    
    ser.close()

start_server = websockets.serve(da_server, "localhost", "8068")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()