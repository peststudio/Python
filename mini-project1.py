# rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    

    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
   

def number_to_name(number):
    # delete the following pass statement and fill in your code below
    
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'


def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    import random
    
    # print a blank line to separate consecutive games
    print '\n' 
    # print the message for the player's choice
    print 'Player chooses', player_choice
    #convert player_choice to player_number
    player_number = name_to_number(player_choice)
    # compute random guess for computer
    comp_number = random.randrange(0,5)
    # convert comp_number to comp_choise
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print 'Computer chooses',comp_choice

    # compute difference of comp_number and player_number modulo five
    diff = (comp_number - player_number) % 5
    # use if/elif/else to determine winner, print winner message
    if diff == 0:
        print 'Player and computer tie!'
    elif diff <= 2:
        print 'Computer wins!'
    else:
        print 'Player wins!'
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
