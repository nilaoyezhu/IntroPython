# template for "Stopwatch: The Game"
import simplegui

# define global variables
interval = 100
height = 160
width = 200
running = False
count = 0

# recommended stop track counters
x = 0
y = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global decimal
    decimal = str(t % 10)
    totSecond = t // 10
    minute = str(totSecond // 60)
    sec = totSecond % 60
    if sec < 10:
        second = '0' + str(sec)
    else:
        second = str(sec)
    return minute + ':' + second + '.' + decimal      
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global running
    timer.start()
    running = True
    
def stop_handler():
    global decimal, running, x, y
    timer.stop()
    if running == True:
        running = False
        y += 1
        if decimal == '0':
            x += 1
    else:
        pass
    
def reset_handler():
    global count, x, y
    timer.stop()
    count = 0
    x = 0
    y = 0
    
# define event handler for timer with 0.1 sec interval
def time_handler():
    global count
    format(count) 
    count += 1
 
# define draw handler
def draw(canvas):
    canvas.draw_text(format(count), (50, 90), 36, 'White')
    canvas.draw_text(str(x) + '/' + str(y), (140, 25), 25, 'Red')
    
# create frame
frame = simplegui.create_frame('Stopwatch', width, height)
frame.add_button('Start', start_handler, 90)
frame.add_button('Stop', stop_handler, 90)
frame.add_button('Reset', reset_handler, 90)
frame.set_draw_handler(draw)

# register event handlers
timer = simplegui.create_timer(interval, time_handler)

# start frame
frame.start()

# Please remember to review the grading rubric
