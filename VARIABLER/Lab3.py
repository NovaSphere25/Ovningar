import math

tal1 = int(input("Mata in tal 1:"))
tal2 = int(input("Mata in tal 2:"))

resultat = tal1**tal2
print(f"Upphöjd: {'{:,}'.format(resultat)}")
resultat = tal1 * tal2
print(f"Gånger: {resultat}")
resultat = int(tal1 / tal2)
print(f"Delat: {resultat}")
resultat = tal1 + tal2
print(f"Plus: {resultat}")
resultat = tal1 - tal2
print(f"Minus: {resultat}")
resultat = tal1 % tal2
print(f"heltalsdividerat: {resultat}")
resultat = tal1 // tal2
print(f"resten: {resultat}")