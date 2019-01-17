# Intro
## Motivation
During the daily usage of computer graphic software, it seems that using digital tablets with its matching pen can do a lot better than just using the mouse.

![tbt2](/img/report/tablet2.png)

However, the tablet itself still holds some drawbacks: not adequately comfortable to be carried along, easily scratched after some period of usage, (for some) some comsumables needed(battery, pentips,etc..) for the whole device.

There should be a way to provide a much more convenient experience.

## Dependency
The programs are written in Python.
- Numpy
- OpenCV
- websocket
- pynput
- bluepy

## Implement
 Structure：
![Structure](/img/report/Structure.jpg)
 There are roughly three parts to realize the function of virtual canvas.
   - Utilizing image processing as the main part on Rpi with an USB camera. (websocket used to send position data)
   - Using pynput library on PC to control the moving the cursor on screen. (like mouse/digital tablet!)
   - Linkit 7697 attached to the pen allowing the clicking/dragging function of the mouse to be trasnfer to PC by BLE connection.
   
### Rpi - USBcamera
`cv2` is how the OpenCV library is imported in code. 
Because we use OpenCV's image capturing and processing functions, `numpy (imported as np)` is used in their input/output to represent the data format of images. 

As beginning, Rpi is connected with the USB camera, as video input device.  Then we assign `cap = cv2.VideoCapture()` so that we can read the frames from `cap` anytime for any part of the processing.  `contours` and some points decisive to shape are drawn and stored after filtering the target, so they can be used to analyze feature of the shape(e.g. pen tip in the whole pen) or decide the relative position.

After the camera "sees" the movement of pentip on the predecided 'canvas', Rpi sends the current position through the web socket to PC, to alter the position of cursor.
#### Detection of canvas
![canvas取得之圖](/img/report/canvas.png)

In code, we specify the canvas part `mask`. By placing a piece of paper and pre-recognizing it, the canvas area is selected (it can be any irregular quadrilateral) and the vertices are recorded to calculate the relative position.

#### Tracking the pen
![tracking畫面圖](/img/report/track.jpg)

While the program's running, it repeatly capture a frame and determine the pentip by drawing contours around marked part(neartip) of pen and getting its center of mass(contained its position).

#### Socket
After binding socket on (host,port) and hosting, Rpi sends the position once per frame to the listening PC(client).
### PC
#### Controlling
`from pynput.mouse import Button, Controller`  Pynput offers the capability of directly read/writing the value of the controller and its left/right button.
`mouse.position(x,y)` can be used to set the position of the cursor.

![Cursor](/img/report/cursor1.png)

#### Socket listening
After the program starts, PC tries connecting its own client to RPi socket until sucessfully connected. Then, PC keeps listening the data sent and use them to change the position of the cursor.

#### BLE server
In PC, executing `ble_setup.py` , defining the Notification-handling and 7697's properties. The notification's handle is assigned to be that button of 7697, so that the "press or not of the left button" can be controlled by the working state of 7697's button through the BLE Notification.
  ```
   if (cHandle== self.button2_handle ):
            #print("button1")
            if self.state ==0:
                mouse = gl.get_value('mouse')
                mouse.press(Button.left)
                self.state =1
            elif self.state ==1 :
                self.state =0
                mouse = gl.get_value('mouse')
                mouse.release(Button.left)
  ```
  ``` 
      def waitNot(self):   ##wait (for) Not(ification)##
        while True:
            if self.dev_button.waitForNotifications(0.1):
                print("not")
  ``` 
  
 ** waitNot() and listen are both added to threading => simultaneously running in threads, listening notification or data sent in.
### Pen
The pen is combined with 7697-linkit to get its clicking function.  The tip of it is marked to help the recognition for now.

![筆的圖](/img/report/pen.jpg)
#### BLE periphral -- 7697
Being connected by PC's BLE server as a peripheral. Set and waited for button state-change notification on PC.
Power supply needed for running the BLE peripheral.


## Reference
- [OpenCV](https://opencv.org/)

- [Socket](https://docs.python.org/3/library/socket.html)

- [pynput](https://pypi.org/project/pynput/)

- [bluepy](https://ianharvey.github.io/bluepy-doc/)
