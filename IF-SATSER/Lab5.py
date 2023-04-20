
correct =False

while(not correct):
    print("Ange vilken kategori den tillhör:")
    category = input("vuxen\npensionär\nstudent\n")
    
    if(category == "pensionär" or category == "student"):
        print("Resan kostar 20 kr")
    elif(category == "vuxen"):
        print("Resan kostar 30 kr")
    else:
        print("Det är inte ett val")
        continue #Input is wrong so reset everthing
    
    temp = input("Är det du angett in korrekt(Y/N)")
    
    if(temp == "Y"):
        correct = True
    else:
        pass
