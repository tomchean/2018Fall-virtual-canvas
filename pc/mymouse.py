from pynput.mouse import Button, Controller
import globalv as gl

def update_mouse(x,y):
    mouse = gl.get_value('mouse')
    my7697 = gl.get_value('my7697')
    if(my7697.my_not.state ==0):
        mouse.move(x,y)
    else:
        print("tmp")
