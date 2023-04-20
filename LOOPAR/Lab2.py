   
tal1 = int(input("Ange start:"))
tal2 = int(input("Ange Stop:"))

for tal in range(tal1, tal2+1):
    print(tal)
    
tal = tal1+1
while(tal != tal2):
    print(tal)
    tal = tal+1