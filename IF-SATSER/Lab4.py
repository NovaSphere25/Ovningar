number1 = input("Tal 1:")
number2 = input("Tal 2:")
number3 = input("Tal 3:")

if(number1 > number2 and number1 > number3):
    big = number1
    temp = 1
elif(number2 > number1 and number2 > number3):
    big = number2
    temp = 2
elif(number3 > number1 and number3 > number2):
    big = number3
    temp = 3
else:
    print("Alla nummer är samma storlek")
    big = "ingen av dem"
    temp = "ingen"

print(f"Det största talet är {big}; som är tal {temp}")