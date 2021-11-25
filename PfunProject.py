def payment():
    pass
def seasonal_discount():
    pass
def package_discount():
    pass
def input_name():
    name=input("Enter your name:")
    
def input_numberOfAdults():                                  #User input for number of adults
    adults = input("Enter the number of adults:")
    b=verifyInput_NumberOfAdults(adults)
    while b==False:
        adults = input("Error! Only accepts integer data type. Try again:")
        b=verifyInput_NumberOfAdults(adults)
    adults=int(adults)    
    print(adults)       
def verifyInput_NumberOfAdults(adults):                     #verification of user input; number of adults
    b=True
    for i in adults:
        if i in "1234567890":
            b=True
        else:
            b=False
            break
    return b    
def input_numberOfChildren():                             #User input for number of children
    children = input("Enter the number of children:")
    b=verifyInput_NumberOfChildren(children)
    while b==False:
        children = input("Error! Only accepts integer data type. Try again:")
        b=verifyInput_NumberOfChildren(children)
    children=int(children)    
    print(children)
def verifyInput_NumberOfChildren(children):                     #verification of user input; number of children
    b=True
    for i in children:
        if i in "1234567890":
            b=True
        else:
            b=False
            break
    return b        
def input_typeOfRoom():
    typeOfRoom = input("Please select your choice of room from the given options: single, double, family, suite:")
    typeOfRoom = typeOfRoom.lower()
    while True:
        if typeOfRoom == "single" or typeOfRoom == "double" or typeOfRoom == "family" or typeOfRoom == "suite":
            break
        else:
            typeOfRoom = input("Error! Try again:")

    print(typeOfRoom)    
def input_durationOfStay():
    durationOfStay=input("Enter the number of nights you wish to stay:")
    b=verifyInput_DurationOfStay(durationOfStay)
    while b==False:
        durationOfStay = input("Error! Only accepts integer data type. Try again:")
        b=verifyInput_DurationOfStay(durationOfStay)
    durationOfStay=int(durationOfStay)    
    print(durationOfStay)
def verifyInput_DurationOfStay(durationOfStay):                     #verification of user input; number of children
    b=True
    for i in durationOfStay:
        if i in "1234567890":
            b=True
        else:
            b=False
            break
    return b    
def facilities():
    pass

singleRoom_perNight = 200.0         #prices in USD
doubleRoom_perNight = 300.0
familyRoom_perNight = 450.0
suiteRoom_perNight = 600.0
breakfast = 100.0
swimmingPool_Gym = 75.0
winter_discount = 15.0
summer_discount = 25.0
familyPackage_discount = 20.0
couplePackage_discount = 15.0
input_name()
input_numberOfAdults()
input_numberOfChildren()
input_typeOfRoom()
input_durationOfStay()
