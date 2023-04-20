answer = "y"
while answer != "n":
    
    tal1 = int(input("Ange start:"))
    tal2 = int(input("Ange Stop:"))
    
    for tal in range(tal1, tal2+1):
        print(tal)
        
    answer = input("Vill du fortsätta(y/n)?")