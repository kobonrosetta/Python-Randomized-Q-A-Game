import sys
import random

ans = True

while ans:
    question = raw_input("**CUSTOM MESSAGE")
    #WELCOME MESSAGE ABOVE^
    
    answers = random.randint(1,9)
    
    if question == "":
        print('Please, type in a question, I said.')
    #OUTPUT IF USER PRESSES ENTER WITHOUT TYPING ANYTHING.
    
    elif answers == 1:
        print "CUSTOM OUTPUT"
    
    elif answers == 2:
        print "CUSTOM OUTPUT"
    
    elif answers == 3:
        print "CUSTOM OUTPUT"
    
    elif answers == 4:
        print "CUSTOM OUTPUT"
    
    elif answers == 5:
        print "CUSTOM OUTPUT"
    
    elif answers == 6:
        print "CUSTOM OUTPUT"
    
    elif answers == 7:
        print "CUSTOM OUTPUT"
    
    elif answers == 8:
        print "CUSTOM OUTPUT"

    elif answers == 9:
        print "CUSTOM OUTPUT"

#TYPE IN DESIRED OUTPUTS ABOVE^