answer = "y"
while answer != "n":
    
    tal1 = int(input("Ange start:"))
    tal2 = int(input("Ange Stop:"))
    
    for tal in range(tal1, tal2+1):
        print(tal)
        
    answer = input("Vill du fortsätta(y/n)?")
        
    #sum = 0        
    #for i in range(0,10):
    #    tal = input(f"Mata in tal nummer {i+1}")
    #    sum = sum + tal
    #    
    #print("Summan av alla talen blev...{sum}")