number1 = input("Tal 1:")
number2 = input("Tal 2:")

if(number1 > number2):
    big = number1
    temp = 1
elif(number2 > number1):
    big = number2
    temp = 2
else:
    print("Bådda nummer är samma storlek")
    big = "ingen av dem"
    temp = "ingen"

print(f"Det största talet är {big}; som är tal {temp}")