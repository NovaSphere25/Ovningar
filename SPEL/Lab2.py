import random

number = random.randint(1,100)
guess = -1
guesses = 0
playing = True

def cal():
    global guess
    global guesses
    global number
    
    guess = -1
    guesses = 0
    number = random.randint(1,100)
    
def menu():
    while(True):
        argument = input("1.Spela\n2.Highscore\n0.Avsluta\n")
        match argument:
            case "0":
                return
            case "1":
                play()
            case "2":
                get_highscores()
            case default:
                print("Inte ett alternativ")
        
def get_highscores():
    scores = []
    with open("highscores.txt", "r") as f:
        for line in f:
            name, score = line.strip().split(",")
            scores.append((name, int(score)))
    
    scores = sorted(scores, key=lambda x: x[1])
    
    num = 1
    for x in scores:
        scores[num-1] = str(num)+"."+str(x)
        num=num+1
    
    print("")
    print("\n".join(scores))
    print("")
        
def write_highscore(name, score):
    with open("highscores.txt", "a") as f:
        f.write(f"{name},{score}\n")

def play_again():
    cal()
    global playing
    
    while(True):
        answer = input("Vill du spela igen (Ja/Nej)?")
        if(answer == "Ja"):
            print("\n")
            print("Gissa ett tal mellan 1 och 100.")
            return
        elif(answer == "Nej"):
            print("Tack för den här gången!")
            playing = False
            return

def play():
    print("Gissa ett tal mellan 1 och 100.")
    cal()
    
    global guesses
    global playing
    
    playing = True
    
    while(playing):
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
            
            temp = input("Vil du spara din rekord?(Y/N)")
            
            if(temp == "y" or temp == "Y"):
                write_highscore(input("Ange namn: "),int(guesses))
            else:
                pass
            
            play_again()
        else:
            print("An unknown Error Has Occurred")

    return

while(True):
    menu()
    break
    



        
        


