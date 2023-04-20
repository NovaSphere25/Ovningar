money = int(input("Hur mycket pengar har du?"))
discount = input("har du rabatt(y/n)").lower() == "y"

if money < 15:
    print("Du kan köpa inget")
elif money <= 25:
    print("Du kan köpa en liten hamburgare" + (" och en pommes frites" if discount else ""))
elif money <= 50:
    print("Du kan köpa en stor hamburgare" + (" och pommes frites" if discount else ""))
elif money <= 60:
    print("Du kan köpa en hamburgare meal med dryck" if discount else "Du kan köpa en stor hamburgare och pommes frites")
else:
    print("Du kan köpa en hamburgare meal med dryck")
