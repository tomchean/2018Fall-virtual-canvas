import asyncio
import time
from pynput.mouse import Button, Controller
from mymouse import *
import socket


async def handle_echo(reader, writer):
    
    data = await reader.read(100)
    message = data.decode()
    
    print("Received %r " % (message))
    buf = message.split(" ")
    update_mouse(int(buf[0]),int(buf[1]))    

    print("Send: %r" % message)
    '''
    writer.write(data)
    await writer.drain()
    '''
    print("Close the client socket")
    writer.close()
    

async def handle_ble(my7697):
    while True:
        my7697.waitNot()
        await asyncio.sleep(0.0001)



class mysocket:
    def __init__(self):
        self.tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        self.tcpServer.bind(('127.0.0.1', 10000)) # IP and PORT   
        self.timeout = 0.1



