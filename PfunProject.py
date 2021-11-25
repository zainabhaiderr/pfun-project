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
def input_arrivalDate():
    date=input("Please enter your date of arrival in the format dd/mm/yyyy:")
    
def input_departureDate():
    pass    
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
def breakfast():
    choice=input("Would you like to include our breakfast facility during your stay? Enter 'y' for yes and 'n' for no:")
    choice=choice.lower()
    while True:
        if choice =="y" or choice=="n":
            break
        else:
            choice=input("Error! Try agian. Enter 'y' for yes and 'n' for no:")
    if choice=="y":
        return True
    else:
        return False
def swimming_gym():
    choice=input("Would you like to avail our swimming pool and gym facility during your stay? Enter 'y' for yes and 'n' for no:")
    choice=choice.lower()
    while True:
        if choice =="y" or choice=="n":
            break
        else:
            choice=input("Error! Try agian. Enter 'y' for yes and 'n' for no:")
    if choice=="y":
        return True
    else:
        return False    
    

singleRoom_perNight = 200.0         #prices in USD
doubleRoom_perNight = 300.0
familyRoom_perNight = 450.0
suiteRoom_perNight = 600.0
breakfast_charges = 100.0
swimmingPool_Gym_charges = 75.0
winter_discount = 15.0
summer_discount = 25.0
familyPackage_discount = 20.0
couplePackage_discount = 15.0
name=input_name()
adults=input_numberOfAdults()
children=input_numberOfChildren()
room=input_typeOfRoom()
duration=input_durationOfStay()
if room!="suite":
    breakfast_included=breakfast()
    swimming_gym_included=swimming_gym()
else:
    breakfast_included=True
    swimming_gym_inlcluded=True
