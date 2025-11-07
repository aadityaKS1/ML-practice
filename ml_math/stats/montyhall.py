import numpy as np
import utils
def monty_hall(switch):
    #all doors have a goat initially
    doors=np.array([0,0,0])

    #randomly decide which door will have a car
    winner_index=np.random.randint(0,3)
    
    #place the car in the winner door
    doors[winner_index]=1
    
    #participate selects a door at random
    choice=np.random.randint(0,3)

    #get the doors that can be opened (host cannot opeon the door chosen or the one with the car)
    openable_doors=[i for i in range(3) if i not in (winner_index,choice)]
    
    #Host opens one of the available doors at random
    door_to_open=np.random.choice(openable_doors)

    #switch to other availabe door(one that is not the orinial cohoice or the opened one)
    if switch:
        choice=[i for i in range(3) if i not in (choice,door_to_open)][0]

    #return 1 if you open  with a car ,0 otherwise
    return doors[choice]

print(monty_hall(True))