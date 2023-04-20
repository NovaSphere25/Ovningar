import random

number = random.randint(1,100)
guess = -1
guesses = 0
p = True

def cal():
    global guess
    global guesses
    global number
    
    guess = -1
    guesses = 0
    number = random.randint(1,100)
    

def play_again():
    
    cal()
    
    global p
    
    while(True):
        answer = input("Vill du spela igen (Ja/Nej)?")
        if(answer == "Ja"):
            print("\n")
            print("Gissa ett tal mellan 1 och 100.")
            return
        elif(answer == "Nej"):
            print("Tack för den här gången!")
            p = False
            break

print("Gissa ett tal mellan 1 och 100.")

cal()

while(p):
    guesses = guesses+1
    guess = input(f"Gissning {guesses}: ")
    
    temp = guess.strip().isdigit()
    
    if(temp == False):
        print("Du kan bara skriva ett tal med siffror. Försök igen!")
    elif(int(guess)<1 or int(guess)>100):
        print("Talet ska vara mellan 1 och 100.")
    elif(int(guess)<number):
        print("Talet är större.")
    elif(int(guess) > number):
        print("Talet är mindre.")
    elif(int(guess) == number):
        print(f"Rätt! Du gissade rätt på {guesses} försök.")
        play_again()
        
    else:
        print("An unknown Error Has Occurred")
        
        


