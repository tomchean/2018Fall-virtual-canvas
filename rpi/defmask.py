import socket
import sys
import cv2
import pickle
import numpy as np
import struct ## new
import zlib

def defmask(frame):
    lower_white=np.array([0,0,46])
    upper_white=np.array([180,50,220])  

    frame = cv2.GaussianBlur(frame, (3,3), 0)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask2 = cv2.inRange(hsv, lower_white, upper_white)

    res = cv2.bitwise_and(frame, frame, mask=mask2)

    frame = cv2.GaussianBlur(res, (5,5), 0)

    canny = cv2.Canny(res, 30, 100)   

    contours, _ = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    c = max(contours, key = cv2.contourArea)

    arclen = cv2.arcLength(c,True)

    approx = cv2.approxPolyDP(c,0.02*arclen,True)    

    approx = approx.reshape((-1,1,2)) 

    rect = np.zeros(frame.shape[:2],dtype = "uint8")

    cv2.fillPoly(frame, [approx], (0, 255, 0))

    return frame, [approx]




if __name__ == "__main__":

    HOST='192.168.43.211'
    PORT=8485

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('Socket created')

    s.bind((HOST,PORT))
    print('Socket bind complete')
    
    s.listen(1)
    print('Socket now listening')

    conn,addr=s.accept()
    cam = cv2.VideoCapture(0)

    cam.set(4, 680)

    img_counter = 0

    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]



    while True:
        ret, frame = cam.read()

        #rect = np.zeros(frame.shape[:2],dtype = "uint8")

        #cv2.imshow('client',frame)
        cv2.waitKey(1)
        frame , approx = defmask(frame)
        
        #cv2.imshow('mask',frame)
        
        result, frame = cv2.imencode('.jpg', frame, encode_param)
    #    data = zlib.compress(pickle.dumps(frame, 0))
        data = pickle.dumps(frame, 0)
        size = len(data)


        #print("{}: {}".format(img_counter, size))
        conn.sendall(struct.pack(">L", size) + data)
        conn.settimeout(0.1)
        try:
            data = conn.recv(30).decode()
            conn.close()
            s.close()
            print(approx)
            np.save("mask.npy",approx)
            break
            
        except:
            continue
        img_counter += 1

    cam.release()