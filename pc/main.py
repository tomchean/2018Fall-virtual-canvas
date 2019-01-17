from ble_setup import * 
import time
from pynput.mouse import Button, Controller
import globalv as gl
import threading
import socket

def listen(self):
    while True:
        try:
            client = socket.socket() 
            client.connect(('192.168.43.211',5000))
            break
        except:
            continue

    while True:
            data = client.recv(1024).decode()
            if not data:
                    break
            print ("from connected  user: " + str(data))
            
            data = str(data).upper()
            print ("sending: " + str(data))
            client.send(data.encode())
            
    client.close()

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
    print ("finish")
