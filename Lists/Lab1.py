tal = []
temp = 0

for x in range(4):
    t = int(input("Mata in ett tal:"))
    tal.append(t)
    
for x in tal:
    if x > temp:
        temp = x
        pos = tal.index(x)+1
            
print(f"Den största tal är: {temp}")
print(f"{temp} var det tal som matades in på plats {pos} ")