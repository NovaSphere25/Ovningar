import random

def roll_dice(die_size):
    return random.randint(1, die_size)

def number_of_dice(die_number, die_size):
    print("Rolling the Dices...")
    print("The values are...")
    
    
    for die in range(0, die_number):
        print(roll_dice(die_size))

Bool= True

while(Bool):
    
    number_of_dice(2,6)
    
    answer = input("Roll the dices again?")
    
    if(answer != "y"):
        Bool = False
    