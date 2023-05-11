import car
import rich

sim = car.Car()

options = ["Turn Left", "Turn Right", "Drive Forward", "Drive Back", "Rest", "Fill Tank", "Exit"]

def menu():
    
    while(True):
        print(f"1.{options[0]}\n2.{options[1]}\n3.{options[2]}\n4.{options[3]}\n5.{options[4]}\n6.{options[5]}\n7.{options[6]}\n")
    
    
        while True:
            try:
                answer = input(" What do you wish to do: (")
                temp = int(answer) - 1
                print(f"\033[1A \033[26C) {options[temp]}")
                break
            except:
                print("\033[1A \033[26C)")
        
        
        match answer:
            case "1":
                sim.travelDirection("left")
            case "2":
                sim.travelDirection("right")
            case "3":
                sim.travelDirection("forward")
            case "4":
                sim.travelDirection("backward")
            case "5":
                sim.rest()
            case "6":
                sim.refill()
            case "7":
                return
            
    


menu()

#res = input("\033[1A \033[9C Write something here:")