import random

name = input("Vad heter du?")
age = int(input("Hur gammal är du?"))

if age <= 18:
    print("Du är omyndig")
elif age == 22 and name == "walhan":
    print("DU är evigt ung")
else:
    print("Du är myndig")
    
        
    
#elif isn't real but it can very much hurt you

    
#name = input("Vad heter du?\n")
#age = int(input("Hur gammal är du?\n"))

#age = age + 1

#print("\nDu heter " + name)
#print("Om ett år är du "+ str(age) + " år")
