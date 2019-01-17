
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
   - Utilizing image processing as the main part on Rpi with an USB camera.
   - Using pynput library on PC to control the moving the cursor on screen. (like mouse/digital tablet!)
   - Linkit 7697 attached to the pen allowing the clicking/dragging function of the mouse to be trasnfer to PC by BLE connection.
### Rpi - USBcamera
`cv2` is how the OpenCV library is imported in code. 
Because we use OpenCV's image capturing and processing functions, `numpy (imported as np)` is used in their input/output to represent the data format of images. 

As beginning, Rpi is connected with the USB camera, as video input device.  Then we assign `cap = cv2.VideoCapture()` so that we can read the frames from `cap` anytime for any part of the processing.  `contours` and some points decisive to shape are drawn and stored after filtering the target, so they can be used to analyze feature of the shape(e.g. pen tip in the whole pen) or decide the relative position.

After the camera "sees" the movement of pentip on the predecided 'canvas', Rpi sends the current position through the web socket to PC, to alter the position of cursor.
#### Detection of canvas
canvas取得之圖
In code, we specify the canvas part `mask`. By placing a piece of paper and pre-recognizing it, the canvas area is selected (it can be any irregular quadrilateral) and the vertices are recorded to calculate the relative position.

#### Tracking the pen
圖
While the program's running, it repeatly capture a frame and determine the pentip by drawing contours around marked part(neartip) of pen and getting its center of mass(contained its position).

#### Socket
After binding socket on (host,port) and building the connection, Rpi sends the position once per frame to the listening PC.
### PC
#### Controlling
`from pynput.mouse import Button, Controller`  Pynput offers the capability of directly read/writing the value of the controller and its left/right button.
`mouse.position(x,y)` can be used to set the position of the cursor.

#### Socket listening
After the program starts, PC tries connecting its own client to RPi socket until sucessfully connected. Then, PC keeps listening the data sent and use them to change the position of the cursor.

#### BLE server
In PC, executing `ble_setup.py` , defining the Notification-handling
或許可以用function執行前後的截圖來呈現
### Pen
筆的圖
#### BLE periphral -- button
ble connection (still toward pynput?)
## Execution
在持有所需的器材時
如何利用GitHub上的檔案執行此功能
## Reference
opencv的

opencv的(依不同部分)

socket?

pynput

bluepy

