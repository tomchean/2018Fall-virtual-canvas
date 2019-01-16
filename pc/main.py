import asyncio
from ble_setup import * 
from mysocket import *
import time
from pynput.mouse import Button, Controller
import globalv as gl
import threading
import socket

def listen(self):
    host = "127.0.0.1"
    port = 5000        
    mySocket = socket.socket()
    mySocket.bind((host,port))
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
            data = conn.recv(1024).decode()
            if not data:
                    break
            print ("from connected  user: " + str(data))
            
            data = str(data).upper()
            print ("sending: " + str(data))
            conn.send(data.encode())
            
    conn.close()

if __name__ == "__main__":
    ##set up global variable
    gl._init()
    mouse = Controller()
    my7697 = ble_7697()
    gl.set_value('mouse',mouse)
    gl.set_value('my7697',my7697)
   

    threads = []
    t1 = threading.Thread(target=my7697.waitNot)
    threads.append(t1)
    t2 = threading.Thread(target=listen)
    threads.append(t2)
    if __name__=='__main__':
        for t in threads:
            t.start()
        for t in threads:
            t.join()
    print ("退出线程")




    '''   
    ### set up receive data loop
    loop = asyncio.get_event_loop()
    coro1 = asyncio.start_server(handle_echo, '192.168.43.211', 8888, loop=loop)
    coro2 = asyncio.ensure_future(handle_ble(my7697))
    task = [coro1,coro2]
    server = loop.run_until_complete(coro1)


    # Serve requests until Ctrl+C is pressed
    print('Serving on {}'.format(server.sockets[0].getsockname()))
    try:
        loop.run_until_complete(asyncio.wait(task))
    except KeyboardInterrupt:
        pass
 
    # Close the server
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

    '''