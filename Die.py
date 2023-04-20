import random

def roll_dice(die_size):
    return random.randint(1, die_size)

while True:
    
    print("What type of Die do you wish to roll?")
    
    print("D4\nD6\nD8\nD10\nD12\nD20\nD100")
    
    while(True):
        type = input(":")

        if(type == "D4" or type == "D6" or type == "D8" or type == "D10" or type == "D12" or type == "D20" or type == "D100"):
            
            break
        else:
            print("Ej Giltigt")
            
    temp = type[1:]
    
    print(f"En {type} kastas, Talet blev {roll_dice(int(temp))}")
    
    svar = input("Vill du kasta en gång till y/n?")
    
    if(svar == "n"):
        break
