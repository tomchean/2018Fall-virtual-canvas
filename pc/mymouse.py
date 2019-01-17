from pynput.mouse import Button, Controller
import globalv as gl

def update_mouse(x,y):
    mouse = gl.get_value('mouse')
    mouse.position = (x,y)
        