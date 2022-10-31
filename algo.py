# An algorithm to catch the rabbit

from random import randint
movement = [-1,1]
rabbitLocation = randint(0,99)

while rabbitLocation > 100 or rabbitLocation < 0:
    rabbitLocation = randint(0,99)
    
count = 0

while count != rabbitLocation:
    rabbitLocation = rabbitLocation + random.choice(movement)
    count += 1
    if count == rabbitLocation:
        print("Got the rabbit at hole {} in {} tries.".format(rabbitLocation, count + 1))
    if count == 100:
        print("Missed the rabbit...")
        print("The rabbit was in hole {}.".format(rabbitLocation))
        break
