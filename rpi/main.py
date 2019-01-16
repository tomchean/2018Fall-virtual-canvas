from mask import *

if __name__ == "__main__":
    
    cap = cv2.VideoCapture(0)
    rect = defmask(cap)
    while(1):
    # get a frame and show
        ret, frame = cap.read()
        if(not frame.data):
            continue
        cv2.imshow('Capture', frame)    