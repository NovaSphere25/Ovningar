milk = input("Hur många paket mjölk som finns kvar?")

if(milk < 10):
    print("Beställ 30 paket")
elif(milk >= 10 or milk <= 20):
    print("Beställ 20 paket")
else:
    print("Du behöver inte beställa någon mjölk")