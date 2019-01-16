import cv2
import numpy as np


def defmask(cap):
    ret, frame = cap.read()
    rect = np.zeros(frame.shape[:2],dtype = "uint8")
    lower_white=np.array([0,0,46])
    upper_white=np.array([180,43,220])
    while(1):
        # get a frame and show
        ret, frame = cap.read()
        cv2.imshow('Capture', frame)    
        frame = cv2.GaussianBlur(frame, (5,5), 0)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask2 = cv2.inRange(hsv, lower_white, upper_white)
        res = cv2.bitwise_and(frame, frame, mask=mask2)
        frame = cv2.GaussianBlur(res, (5,5), 0)
        canny = cv2.Canny(res, 30, 100)   
        _, contours, _ = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        c = max(contours, key = cv2.contourArea)
        arclen = cv2.arcLength(c,True)
        approx = cv2.approxPolyDP(c,0.02*arclen,True)    
        approx = approx.reshape((-1,1,2))
        rect = np.zeros(frame.shape[:2],dtype = "uint8")
        cv2.fillPoly(rect, [approx], (255, 255, 255))
        res = cv2.bitwise_and(frame, frame, mask=rect)
        cv2.imshow('Result', res)
        # detect blue
        if cv2.waitKey(1) & 0xFF == ord('q'):
            #cap.release()
            cv2.destroyAllWindows()
            break
    cv2.destroyAllWindows()
    return rect
