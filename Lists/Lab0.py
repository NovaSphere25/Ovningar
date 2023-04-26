namn = "Stefan"
namn = namn + " Holmberg" + " " + "heter han"
antal = len(namn)
As = 0

for x in range(len(namn)):
    if(namn[x] == "a"):
        As = As + 1

print(f"Number of A's: {As}")

namn = "Hejsan"
d = namn[0]

name = input("Vad heter du?")
first = name[0]
print(f"Ditt namn börjar på {first}")

fult = "läxa"
fult2 = "grönsaker"

while True:
    txt = input("Skriv in:")
    txt = txt.lower
    if txt.find(fult) == -1:
        if txt.find(fult2) == -1:
            print(txt)
            continue
    print("No")
    break
    
    print(txt)