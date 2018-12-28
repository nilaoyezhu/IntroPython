# implementation of card game - Memory

import simplegui
import random
Semirange = 8

# helper function to initialize globals
def new_game():
    global cards
    set1 = range(Semirange)
    set2 = range(Semirange)
    random.shuffle(set1)
    random.shuffle(set2)
    cards = set1 + set2

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards
    for card_index in range(len(cards)):
        card_pos = 50 * card_index
        canvas.draw_polygon([[card_pos, 0], [card_pos, 100],
                           [card_pos + 50, 0], [card_pos + 
                           50, 100]], 1, "Green")
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
