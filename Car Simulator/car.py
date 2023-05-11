from rich import print
{#import directionality


#north = directionality('nouth')
#south = directionality('south')
#east = directionality('east')
#west = directionality('west')

#north.opposite = south
#east.opposite = west
}
class Car():
    
    heading = 'North'
    gas = 20
    tired = 0
    
    specialCase = 0
    
    def turnCarLeft(self):
        if self.heading == "North":
            self.heading = 'West'
        elif self.heading == "South":
            self.heading = 'East'
        elif self.heading == "East":            
            self.heading = 'North'
        elif self.heading == "West":
            self.heading = 'South'
                    
    def turnCarRight(self):
        if self.heading == "North":      
            self.heading = 'East'
        elif self.heading == "South":      
            self.heading = 'West'
        elif self.heading == "East":      
            self.heading = 'South'
        elif self.heading == "West":      
            self.heading = 'North'
    
    def travelDirection(self, direction):
        if(self.testGas()):
            self.testTiredness()
            if direction == 'left':
                self.turnCarLeft()
                self.specialCase = 0
                self.printDisplay(direction)
            if direction == 'right':
                self.turnCarRight()
                self.specialCase = 0
                self.printDisplay(direction)
            if direction == 'forward':
                self.specialCase = 1
                self.printDisplay(direction)
            if direction == 'backward':
                self.specialCase = 2
                self.printDisplay(direction)
                
    def printDisplay(self, direction):
        if self.specialCase == 0:
            print(f"\n\nThe Driver turned and drived {direction}\n")
            print(f"   [bold white]Car Direction: {self.heading}[bold white]\n")
            print(f"   [bold green]Gas: {self.gas}/20[bold green]\n")
            print(f"   [bold red]Drivers Tiredness: {self.tired}/10[bold red]\n")
        if self.specialCase == 1:
            print(f"\n\nThe Driver Drove Forwards\n")
            print(f"   [bold white]Car Direction: {self.heading}[bold white]\n")
            print(f"   [bold green]Gas: {self.gas}/20[bold green]\n")
            print(f"   [bold red]Drivers Tiredness: {self.tired}/10[bold red]\n")
        if self.specialCase == 2:
            print(f"\n\nThe Driver Reversed\n")
            print(f"   [bold white]Car Direction: {self.heading}[bold white]\n")
            print(f"   [bold green]Gas: {self.gas}/20[bold green]\n")
            print(f"   [bold red]Drivers Tiredness: {self.tired}/10[bold red]\n")
        
    def testGas(self):
        if(self.gas > 0):
            self.gas = self.gas - 1
            return True
        print("\n\n[bold red]YOU ARE OUT OF GAS[bold red]\n")
        return False
    
    def testTiredness(self):
        if self.tired >= 10:
            print("\n\n[bold red]You HAVE MAXED OUT YOUR TIREDNESS[bold red]\n")
        elif self.tired >= 6:
            print("\n\n[bold dark_orange]You ARE BEGINNING TO MAX OUT YOUR TIREDNESS[bold dark_orange]\n")
        else:
            pass
        self.tired = self.tired + 1
    
    def rest(self):
        self.tired = 0
        print(f"\n\n[bold green]You have rested yourself[bold green]\n")
    
    def refill(self):
        self.gas = 20
        print(f"\n\n[bold green]Gas has been refilled[bold green]\n")
        