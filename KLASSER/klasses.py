from dataclasses import dataclass


@dataclass
class Rectangle:
    Width: int = 0
    Height: int = 0
    
def calculateArea(rect):
    area = rect.Width * rect.Height
    return area

r = Rectangle()
r.Width = 20
r.Height = 10
print(calculateArea(r))
r2 = Rectangle()
r2.Width = 10
r2.Height = 3
print(calculateArea(r2))


@dataclass
class HouseBluePrint:
    Color: str = ""
    NrOfWindows: int = 0
    Address: str = ""
    
    
mittHus = HouseBluePrint()
mittHus.Color = "Brown"
mittHus.NrOfWindows = 12
mittHus.Address = "Testgatan 12"

syrransHus = HouseBluePrint()
syrransHus.Color = "Rött"
syrransHus.NrOfWindows = 9
syrransHus.Address = "Testgatan 13"