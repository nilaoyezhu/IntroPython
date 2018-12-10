# Echo mouse click in console
import simplegui
###################################################
# Student should enter code below

def mouse_handler(position):
    print("Mouse click at " + str(position))

frame = simplegui.create_frame("Mouse Echo", 300, 300)
frame.set_mouseclick_handler(mouse_handler)
frame.start()
