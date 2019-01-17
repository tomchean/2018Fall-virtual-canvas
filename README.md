# 2018Fall-Virtual-Canvas

This is a project that utilizes image processing to realize a canvas

## Motivation
During the daily usage of computer graphic software, it seems that using digital tablets with its matching pen can do a lot better than just using the mouse.

![tbt2](/img/report/tablet2.png)

However, the tablet itself still holds some drawbacks: not adequately comfortable to be carried along, easily scratched after some period of usage, (for some) some comsumables needed(battery, pentips,etc..) for the whole device.

There should be a way to provide a much more convenient experience.

## Dependency
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
概述opencv?
#### Detection of canvas
canvas取得之圖
或許有一小段示意程式碼?
#### Tracking the pen
圖
示意講解?
### PC
pynput語法示意
或許可以用function執行前後的截圖來呈現
### Pen
筆的圖
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

