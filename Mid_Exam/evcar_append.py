
"""
Name :pannika nareeloed
ID: 364211760025
Group: MIT221
"""

# display
def display_Ev_Car():
    if len(my_evcar) ==0:
        print("You had Ev_Car data")
    else:
        print(f'You had {len(my_evcar)}follwing:')
    for x in my_evcar:
        x.evcar_detail()
        print("\n")

#option
def display_option():
    select = 0
    print("Welcome to Vehicle Data Store System (VDSS)")
    print("1.Add Ev_Car ")
    print("2.Display all Ev_Car")
    print("3.exit")
    select = int(input("select(1-3)? : "))
    if select == 1:
        input_Ev_Car()
    elif select == 2:
        display_Ev_Car()
    elif select == 3:
        print("thank you.")
        exit(0)
    else:
        print("Please, select number 1-3.")

#input data
def input_Ev_Car():
    Brand = input("Enter Ev_Car Brand : ")
    Model = input("Enter Ev_Car Model : ")
    Motor = input("Enter Ev_Car Motor : ")
    Horsepower = int(input("Enter Ev_Car Horse power : "))
    Batterysize = input("Enter Ev_Car Batterysize : ")
    Range = input("Enter Ev_Car Range : ")
    Price = float(input("Enter Ev_Car Price : "))
    return (Brand,Model,Motor,Horsepower,Batterysize,Range,Price) # return as tuple
    my_evcar.append(Ev_Car(Brand,Model,Motor,Horsepower,Batterysize,Range,Price))
    print("\n----------------------------------")
    print("Already add Ev_Car to store.")
    print("\n----------------------------------")

my_evcar = []
s = 0
while s == 0:
     display_option()
