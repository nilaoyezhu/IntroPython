# Image positioning problem

###################################################
# Student should enter code below

import simplegui

# global constants
WIDTH = 400
HEIGHT = 300
position = [WIDTH / 2, HEIGHT / 2]

# load test image
image = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/asteroid.png')
imageW = image.get_width()
imageH = image.get_height()
imageC = [imageW / 2, imageH / 2]
# mouseclick handler
def click(pos):
    global position
    position = pos
    
# draw handler
def draw(canvas):
    canvas.draw_image(image, imageC, [imageW, imageH], 
                      position, [WIDTH, HEIGHT])
    
# create frame and register draw handler    
frame = simplegui.create_frame("Test image", WIDTH, HEIGHT)
frame.set_canvas_background("Gray")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

# start frame
frame.start()
