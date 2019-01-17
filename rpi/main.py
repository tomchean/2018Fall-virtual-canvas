import cv2
import numpy as np
import socket
import time


if __name__ == "__main__":

    host = "192.168.43.211"
    port = 5000        
    mySocket = socket.socket()

    mySocket.bind((host,port))

    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))

    cap = cv2.VideoCapture(0)
    cap.set(4,480)
    _, image = cap.read()

    lower = np.array([100, 43, 46])
    upper = np.array([124, 255, 255])

    #construct mask
    rect = np.zeros(image.shape[:2],dtype = "uint8")
    c = np.load("mask.npy")
    cv2.fillPoly(rect, c , (255, 255, 255))
    c = c.reshape((-1,2))
    ymin = c[:,1].min(0)
    ymax = c[:,1].max(0)
    xmax = c[:,0].max(0)
    xmin = c[:,0].min(0)
    multx = 1920/(xmax - xmin)
    multy = 1080/(ymax - ymin)

    print(xmax,xmin,ymax,ymin)

    while(1):

        # Capture Video from Camera
        _, image = cap.read()
        image = cv2.bitwise_and(image,image, mask=rect)
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        filtered = cv2.inRange(hsv, lower, upper)
        blurred = cv2.GaussianBlur(filtered, (15, 15), 0)

        # find contours in the image
        #(_, cnts, _) = cv2.findContours(blurred.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts, _ = cv2.findContours(blurred.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if(len(cnts)):
            c = max(cnts, key = cv2.contourArea)
            M = cv2.moments(c)
            '''
            extBot = tuple(c[c[:, :, 1].argmax()][0])
            x = 1920 - (extBot[0] - xmin)*multx
            y = 1080 -(extBot[1] - ymin)*multy
            '''
            x = 1920 - (int(M["m10"] / M["m00"]) - xmin)*multx
            y = 1080 -(int(M["m01"] / M["m00"]) - ymin)*multy
            msg = str(x)+" "+str(y)+" "
            print(msg)
            conn.send(msg.encode('utf-8')) 
            
            #cv2.circle(image, extBot , 3, (255, 0, 0), -1)
            #print(extBot)
            
        #cv2.imshow("Tracking", image)
        #cv2.waitKey(0.1)
    conn.close()
    mySocket.close()
