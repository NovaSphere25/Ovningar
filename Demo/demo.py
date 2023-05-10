# om man handlat för  minst 1000 kr får man 100kr i rabatt
# om man är medlem i kundklubb får man 2% rabatt
# om man handlat för minst 5000 kr man 1% rabatt på priset över 5000
# vi ska skriva en calculateDiscountedPrice(totalPrice) som implementerar dessa regler

def calculateDiscountedPrice(totalPrice, isMember):
    rabatt = 0
    if totalPrice >= 5000:
        rabatt = rabatt + ((totalPrice - 5000) * 0.01)
    if isMember:
        rabatt = rabatt + (totalPrice * 0.02)
    if totalPrice > 1000:
        rabatt = rabatt + 100
    return totalPrice - rabatt