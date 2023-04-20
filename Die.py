import random

def roll_dice(die_size):
    return random.randint(1, die_size)

while True:
    
    print("What type of Die do you wish to roll?")
    
    print("D4\nD6\nD8\nD10\nD12\nD20\nD100")
    
    type = input(":")
    
    temp = type[1:]
    roll_dice(temp)
    
    print(f"En {type} kastas, Talet blev {roll_dice(temp)}")
    
    svar = input("Vill du kasta en gång till y/n?")
    
    if(svar == "n"):
        break
