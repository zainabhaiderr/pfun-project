import datetime as dt

def input_name():                          #Customer Name input
    print("Welcome to Hotel Trivago! Please answer the following questions to complete your hotel reservation. Thank you!")
    name=input("Enter your name:")
    b=True
    while True:
        for i in name:
            if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ":
                b=True
            else:
                b=False
                break
        if b==True:
            break
        else:
            name=input("Error! Please enter valid name using only alphabets. Try again! Enter your name:")
    return name
    
def input_numberOfAdults():                                  #User input for number of adults
    adults = input("Enter the number of adults:")
    b=verifyInput_NumberInput(adults)                        #Calling function for verifying data type
    while b==False:
        adults = input("Error! Only accepts integer data type. Try again:")
        b=verifyInput_NumberInput(adults)
    adults=int(adults)    
    return(adults)       

def input_numberOfChildren():                             #User input for number of children
    children = input("Enter the number of children:")
    b=verifyInput_NumberInput(children)                   #Calling function for verifying data type
    while b==False:
        children = input("Error! Only accepts integer data type. Try again:")
        b=verifyInput_NumberInput(children)
    children=int(children)    
    return(children)

def verifyInput_NumberInput(value):                     #verification of any numeric user input (Number of adults, number of children)
    b=True
    for i in value:
        if i in "1234567890":
            b=True
        else:
            b=False
            break
    return b    


def input_typeOfRoom():               #User input for type of room
    typeOfRoom = input("Please select your choice of room from the given options: single, double, family, suite:")         #choosing from 4 options 
    typeOfRoom = typeOfRoom.lower()
    while True:
        if typeOfRoom == "single" or typeOfRoom == "double" or typeOfRoom == "family" or typeOfRoom == "suite":            #Verifying input 
            break
        else:
            typeOfRoom = input("Error! Try again:")
            typeOfRoom = typeOfRoom.lower()
    return(typeOfRoom)

def input_numberOfRooms():                                                 #User Input for number of rooms
    rooms=input("Enter the number of rooms you wish to book:")
    while True:                                                            #verifying data type
        for i in rooms:
            if i in "1234567890":
                b=True
            else:
                b=False
                break
        if b==True:
            break
        else:
            rooms=input("Error! Only accepts numeric value. Enter the number of rooms you wish to book:")
    rooms=int(rooms)
    return rooms
            
    
def input_arrivalDate():                                  #User input for date of arrival
    import datetime as dt                                 #using datetime module
    currentDate=dt.datetime.now()                         #Using datetime module to find current date
    date=input("Please enter your date of arrival in the format dd/mm/yyyy:")
    while True:
        b=verifyDate(date)                                    #verifying date format and input values of day and month by calling function verifyDate
        while b==False:
            date=input("Try Again!")
            b=verifyDate(date)        
        
        day,month,year = date.split('/')                      #splitting input date into day, month, year for more verification
        day=int(day)
        month=int(month)
        year=int(year)
        date1=dt.datetime.strptime(date, "%d/%m/%Y")          #writting input date in datetime module format 

        if date1<=currentDate:                          #Displaying error if date is less than present date
            date=input("Invalid date! Date has to be greater than present date. Try again!")
        else:
            break       
    return date
def input_departureDate(arrivalDate):                     #User input for date of departure
    import datetime as dt                                 #using datetime module 
    currentDate=dt.datetime.now()                         #Using datetime module to find current date 
    date=input("Please enter your date of departure in the format dd/mm/yyyy:")
    while True:
        b=verifyDate(date)                               #verifying format and input values of day and month by calling function verifyDate
        while b==False:
            date=input("Try Again!")
            b=verifyDate(date)
        
        day,month,year = date.split('/')                       #splitting input date into day, month, year for more verification
        day=int(day)
        month=int(month)
        year=int(year)
        arrivalday=int(arrivalDate[0:2])                     #splitting arrivalDate parameter into day, month, year for more verification
        arrivalmonth=int(arrivalDate[3:5])
        arrivalyear=int(arrivalDate[6:10])
        departureday=int(date[0:2])                    #splitting input departureDate into day, month, year for more verification
        departuremonth=int(date[3:5])
        departureyear=int(date[6:10])
        AD=dt.datetime(arrivalyear,arrivalmonth,arrivalday)       #converting arrival date into datetime format for comparing
        DD=dt.datetime(departureyear,departuremonth,departureday) #converting departure date into datetime format for comparing
        date1=dt.datetime.strptime(date, "%d/%m/%Y")         #writting input date in datetime module format

     
        if date1<=currentDate:                          #Displaying error if date is less than present date
            date=input("Invalid date! Date has to be greater than present date. Try again!")
        elif DD<=AD:                                                          #Displaying error if departure date is less than arrival date
            date=input("Error! Departure date can not be before or the same as the arrival date. Try again:")
        else:
            break       
    return date
       
def verifyDate(date):                                    #funtion for checkingdate format and if input value of day and month in arrival and departure date is within range 
        if len(date)==10:                                #check #1 for format
            if date[2] and date[5]=="/":                 #check #2 for format
                if date[0]in "1234567890" and date[1]in "1234567890" and date[3]in "1234567890" and date[4]in "1234567890" and date[6]in "1234567890" and date[7]in "1234567890" and date[8]in "1234567890" and date[9]in "1234567890":    #check #3 for format
                    day,month,year = date.split('/')                       #splitting input date into day, month, year for more verification
                    day=int(day)
                    month=int(month)
                    year=int(year)
                    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:   #assigning max value of days depending on month for verification
                        max_days=31
                    elif month==4 or month==6 or month==9 or month==11:
                        max_days=30
                    elif month==2 and (year%4==0 and year%100!=0 or year%400==0):                                           #checking for leap year
                        max_days=29
                    elif month==2:
                        max_days=28
                    else:
                        max_days=31
            
                    if (month<1 or month>12) and (day<1 or day>max_days):
                        print("Invalid date! Month and day is out of range.")    #Displaying error if month value is out of range
                        return False
                    elif month<1 or month>12:
                        print("Invalid date! Month is out of range.")    #Displaying error if month value is out of range
                        return False
                    elif day<1 or day>max_days:
                        print("Invalid date! Day is out of range.")      #Displaying error if day value is out of range
                        return False
                    else:
                        return True
                else:
                    print("Error! Invalid format. Please enter your date in the format dd/mm/yyyy")
                    return False
            else:
                print("Error! Invalid format. Please enter your date in the format dd/mm/yyyy")
                return False                
        else:
            print("Error! Invalid format. Please enter your date in the format dd/mm/yyyy")
            return False
   
def breakfast():                                                             #User input for availing of breakfast
    choice=input("Would you like to avail our breakfast facility during your stay? Enter 'y' for yes and 'n' for no:")
    choice=choice.lower()
    while True:
        if choice =="y" or choice=="n":
            break
        else:
            choice=input("Error! Try agian. Enter 'y' for yes and 'n' for no:")
            choice=choice.lower()
    if choice=="y":
        return True
    else:
        return False
def swimming_gym():                                                         #User input for availing swimming pool and gym
    choice=input("Would you like to avail our swimming pool and gym facility during your stay? Enter 'y' for yes and 'n' for no:")
    choice=choice.lower()
    while True:
        if choice =="y" or choice=="n":
            break
        else:
            choice=input("Error! Try agian. Enter 'y' for yes and 'n' for no:")
            choice=choice.lower()
    if choice=="y":
        return True
    else:
        return False

def payment(numberOfRooms, duration, room, breakfast_included, swimming_gym_inlcuded):      #calculating total bill using parameters depending on duration of stay, type of room, number of rooms, breakfast, swimming pool and gym
    singleRoom_perNight = 200.0         #Initialising fixed prices of rooms and facilities, prices in USD
    doubleRoom_perNight = 300.0
    familyRoom_perNight = 450.0
    suiteRoom_perNight = 600.0
    breakfast_charge = 100.0
    swimmingPool_Gym_charge = 75.0
    totalBill=0
    if room=="single":
        totalBill+= singleRoom_perNight*duration*numberOfRooms
    elif room=="double":
        totalBill+= doubleRoom_perNight*duration*numberOfRooms
    elif room=="family":
        totalBill+= familyRoom_perNight*duration*numberOfRooms
    elif room=="suite":
        totalBill+= suiteRoom_perNight*duration*numberOfRooms

    if room!="suite":                #Breakfast, swmming pool and gym facility included for type of room suite.
        if breakfast_included==True:
            totalBill+=breakfast_charge
        if swimming_gym_included==True:
            totalBill+=swimmingPool_Gym_charge
    return totalBill
    

def seasonal_discount(arrivalMonth):      #Seasonal discount applicable for winters(Dec, Jan) and summer(June, July). Depends on month of arrival
    winter_discount = 15.0                #15% discount for winter
    summer_discount = 25.0                #25% discount for summer
    if arrivalMonth==6 or arrivalMonth==7:
        return summer_discount
    elif arrivalMonth==12 or arrivalMonth==1:
        return winter_discount
    else:
        return 0 
def package_discount(adults , children):      #Family and couple package applicable
    familyPackage_discount = 20.0             #20% discount for Family package 
    couplePackage_discount = 15.0             #15% discount for Couple package
    if adults>1 and children>2:             #applicable on families of more than 1 adult and more than 2 children
        return familyPackage_discount
    elif adults==2 and children==0:
        return couplePackage_discount
    else:
        return 0


name=input_name()
adults=input_numberOfAdults()
children=input_numberOfChildren()
room=input_typeOfRoom()
numberOfRooms = input_numberOfRooms()
arrivalDate = input_arrivalDate()
departureDate = input_departureDate(arrivalDate)
arrivalday=int(arrivalDate[0:2])                       #splitting input arrivalDate into day, month, year 
arrivalmonth=int(arrivalDate[3:5])
arrivalyear=int(arrivalDate[6:10])
departureday=int(departureDate[0:2])                   #splitting input departurelDate into day, month, year 
departuremonth=int(departureDate[3:5])
departureyear=int(departureDate[6:10])
AD=dt.datetime(arrivalyear,arrivalmonth,arrivalday)        #converting arrival date into datetime format 
DD=dt.datetime(departureyear,departuremonth,departureday)  #converting departure date into datetime format 
difference=""
difference = str(DD-AD)                                    #using arrival and departure dates to calculate duration of stay 
duration=int(difference[0:2])                              #converting duration of stay into integer value
if room!="suite":                                          #breakfast. swimming pool and gym facility already included for suite                        
    breakfast_included=breakfast()                         
    swimming_gym_included=swimming_gym()
else:
    breakfast_included=True
    swimming_gym_included=True
total_bill = payment(numberOfRooms, duration, room, breakfast_included, swimming_gym_included)
seasonalDiscount=seasonal_discount(arrivalmonth)
packageDiscount=package_discount(adults, children)
total_discount=seasonalDiscount + packageDiscount
finalBill=total_bill*((100-total_discount)/100)           #applysing discount to find final amont
number_of_people = adults+children
if breakfast_included==True:
    breakfast="Yes"
else:
    breakfast="No"

if swimming_gym_included==True:
    swimmingGym="Yes"
else:
    swimmingGym="No"

discountMoney=finalBill-total_bill                      #calculating money deducted due to discount for ouput
print("Your reciept will automatically be generated and will open in a new tab. Thank you for your reservation! Have a good day!")






#Using GUI Tkinter for ouput 
from tkinter import *
root = Tk()
root.title("Receipt")
root.iconbitmap("T1.ico")

#Defining the labels
myLabel=Label(root, text="Hotel Trivago")
myLabel1=Label(root, text="Number of People ")
myLabel2=Label(root, text=str(number_of_people))
myLabel3=Label(root, text="Number of Rooms ")
myLabel4=Label(root, text=str(numberOfRooms))
myLabel5=Label(root, text="Type of room ")
myLabel6=Label(root, text=room)
myLabel7=Label(root, text="Breakfast ")
myLabel8=Label(root, text=breakfast)
myLabel9=Label(root, text="Swimming Pool and Gym ")
myLabel10=Label(root, text=swimmingGym)
myLabel11=Label(root, text="Seasonal Discount ")
myLabel12=Label(root, text=str(seasonalDiscount)+"%")
myLabel13=Label(root, text="Package Discount ")
myLabel14=Label(root, text=str(packageDiscount)+"%")
myLabel15=Label(root, text="Total Amount ")
myLabel16=Label(root, text="$"+str(total_bill))
myLabel17=Label(root, text="Discount ")
myLabel18=Label(root, text=discountMoney)
myLabel19=Label(root, text="Final Amount ")
myLabel20=Label(root, text="$"+str(finalBill))
myLabel21=Label(root, text="Customer Name ")
myLabel22=Label(root, text=name)
myLabel23=Label(root, text="Arrival Date ")
myLabel24=Label(root, text=arrivalDate)
myLabel25=Label(root, text="Departure Date ")
myLabel26=Label(root, text=departureDate)
myLabel27=Label(root, text="                                                  ")



#Putting the labels on screen
myLabel.grid(row=0, column=1)
myLabel1.grid(row=4, column=0)
myLabel2.grid(row=4, column=2)
myLabel3.grid(row=5, column=0)
myLabel4.grid(row=5, column=2)
myLabel5.grid(row=6, column=0)
myLabel6.grid(row=6, column=2)
myLabel7.grid(row=7, column=0)
myLabel8.grid(row=7, column=2)
myLabel9.grid(row=8, column=0)
myLabel10.grid(row=8, column=2)
myLabel11.grid(row=9, column=0)
myLabel12.grid(row=9, column=2)
myLabel13.grid(row=10, column=0)
myLabel14.grid(row=10, column=2)
myLabel15.grid(row=11, column=0)
myLabel16.grid(row=11, column=2)
myLabel17.grid(row=12, column=0)
myLabel18.grid(row=12, column=2)
myLabel19.grid(row=13, column=0)
myLabel20.grid(row=13, column=2)
myLabel21.grid(row=1, column=0)
myLabel22.grid(row=1, column=2)
myLabel23.grid(row=2, column=0)
myLabel24.grid(row=2, column=2)
myLabel25.grid(row=3, column=0)
myLabel26.grid(row=3, column=2)
myLabel27.grid(row=14)
myButton=Button(root, text="Print Receipt", fg="White", bg="black", borderwidth=5, command=root.destroy)
myButton.grid(row=15, column=2)
root.mainloop()
