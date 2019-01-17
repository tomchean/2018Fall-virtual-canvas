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

=========分隔線==========
another text here
```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/chiachip/2018-virtual-canvas/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
