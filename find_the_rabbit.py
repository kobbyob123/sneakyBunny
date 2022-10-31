# There are 100 holes in farm numbered 0 - 99
# A rabbit is randomly placed in a hole 
# You are to guess the number of the hole the rabbit was put in 10 tries - (Kinda impossible tho)
# The rabbit moves to an adjacent hole after every wrong guess 
# It cannot stay inside the same hole after a wrong guess
# eg: if the rabbit was in hole 5, after a wrong guess it can only move to hole 4 or 6

import random
from random import randint
movement = [-1,1]
rabbitLocation = randint(0,99)

while rabbitLocation > 100 or rabbitLocation < 0:
    rabbitLocation = randint(0,99)
tries = 0
# flag = 0

print("Press 'q' to quit the program.")
userChoice = input("Which hole do you think the rabbit is?\n")
'''
while flag == 0:
    if userChoice == 'q':
        break
'''
while int(userChoice) > 99 or int(userChoice) < 0:
    userChoice = input("Please choose a valid hole?\n")

while int(userChoice) != rabbitLocation:
    tries += 1
    
    print("Try again, you have {} tries left.".format(10 - tries))
    rabbitLocation = rabbitLocation + random.choice(movement)
    if rabbitLocation > 99:
        rabbitLocation = 98
    elif rabbitLocation < 0:
        rabbitLocation = 1
    
    userChoice = input("\n")
    if userChoice == 'q':
        print("\nYou gave up. The rabbit was in hole {}.".format(rabbitLocation))
        break
    while int(userChoice) > 99 or int(userChoice) < 0:
        userChoice = input("Please choose a valid hole?\n")
    
    if tries == 9:
        print("You've exhausted your tries...")
        print("\nThe rabbit was in hole {}.".format(rabbitLocation))
        break
    if int(userChoice) == rabbitLocation:
        print("\nYou found the rabbit!!!")
