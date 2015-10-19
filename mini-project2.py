# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math
number_range = 100
secret_number = 0
guesses = 0
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here

    global secret_number
    global guesses
    secret_number = random.randrange(0,number_range)
    guesses = int(math.ceil(math.log(number_range,2)))
    print "The range is [0," + str(number_range) + ")"
    print "You have", guesses, "guesses"
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    
    global number_range
    number_range = 100
    print '\n'
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    
    global number_range
    number_range = 1000
    print '\n'
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    global secret_number
    global guesses
    try:
        int_guess = int(guess)
    except:
        print "Invalid Guess, try again"
        return
    print "Guess was", guess
    if int_guess == secret_number:
        print 'Correct'
        print '\n'
        new_game()
    else:
        guesses -= 1
        if guesses == 0:
            print "The correrct number is", secret_number
            print "You Lose"
            print '\n'
            new_game()
        else:
            if int_guess < secret_number:
                print 'Higher'
            elif int_guess > secret_number:
                print 'Lower'
            print guesses, "guesses left"
        
    
# create frame
new_frame = simplegui.create_frame("Guess the Number",200,300)

# register event handlers for control elements and start frame
new_frame.add_input("Your Guess",input_guess,100)
new_frame.add_button("New Game",new_game,200)
new_frame.add_button("Range is [0,100)",range100,200)
new_frame.add_button("Range is [0,1000)",range1000,200)
new_frame.start()
# call new_game 
new_game()


# always remember to check your completed program against the grading rubric

