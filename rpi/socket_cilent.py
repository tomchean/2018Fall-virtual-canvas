'''
import socket
import time


client = socket.socket() # 聲明socket類型，同時生成socket連接對象
client.connect(('192.168.43.64',5000))

while True:
  #msg = input('>>:').strip()
  msg = '1 1'
  if len(msg) == 0:continue
  client.send(msg.encode('utf-8')) 
  time.sleep(0.01)

client.close()

import asyncio
import time

async def tcp_echo_client(message, loop):
    reader, writer = await asyncio.open_connection('192.168.43.64', 8888, loop=loop)

    print('Send: %r' % message)
    writer.write(message.encode())
    
    
    data = await reader.read(100)
    print('Received: %r' % data.decode())
    
    print('Close the socket')
    writer.close()

while True:
  #message = input('>>:').strip()
  message = '1 0'
  loop = asyncio.get_event_loop()
  loop.run_until_complete(tcp_echo_client(message, loop))
  time.sleep(0.01)
loop.close()
'''


import socket
import cv2
import numpy

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

TCP_IP = "127.0.0.1"
TCP_PORT = 8002
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(True)
conn, addr = s.accept()
while 1:
    length = recvall(conn,16)
    stringData = recvall(conn, int(length))
    data = numpy.fromstring(stringData, dtype='uint8')
    decimg=cv2.imdecode(data,1)
    cv2.imshow('SERVER',decimg)
    cv2.waitKey(30)

s.close()
cv2.destroyAllWindows()