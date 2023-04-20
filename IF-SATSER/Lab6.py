year = input("Mata in sitt födelseår?")

if(int(int(year)) >= 1980 and int(year) < 1990):
    print("Du är född på 1980-talet")
elif(int(year) >= 1990 and int(year) <2000):
    print("Du är född på 1990-talet")
else:
    print("Du är inte född på 1990 eller 1980-talen.")