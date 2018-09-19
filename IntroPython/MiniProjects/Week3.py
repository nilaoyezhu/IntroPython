# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number = 0

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    new_game()
    global count
    count = 7
    print 'New Game. Range is [0,100).'
    print 'Number of remaining guesses is ' + str(count)
    print
    global secret_number
    secret_number = random.randint(0,99)

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    new_game()
    global count
    count = 10
    print 'New Game. Range is [0,1000).'
    print 'Number of remaining guesses is ' + str(count)
    print
    global secret_number
    secret_number = random.randint(0,999)
    
def input_guess(guess):
    # main game logic goes here	
    global secret_number
    global count
    guess_number = int(guess)
    print "Your guess was " + guess
    count = count - 1
    if count > 0:
        print "Number of remaining guesses is " + str(count)
        if secret_number > guess_number:
            print "Higher!"
            print
        elif secret_number < guess_number:
            print "Lower!"
            print
        else:
            print "Correct!"
            print
            range100()
    elif count == 0:
        print "You ran out of guesses.  The number was " + str(secret_number)
        print
        if secret_number > 99:
            range1000()
        else:
            range100()
    
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)
frame.add_button("Range is [0,100)", range100)
frame.add_button("Range is [0,1000)", range1000)
frame.add_input("Guess:", input_guess, 100)

frame.start()
# register event handlers for control elements and start frame


# call new_game 
range100()

# always remember to check your completed program against the grading rubric
