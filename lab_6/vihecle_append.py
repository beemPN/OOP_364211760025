from Vehicle import Vehicle
# display
def display_Vehicle():
    if len(my_vehicle) ==0:
        print("You had Vehicle data")
    else:
        print(f'You had {len(my_vehicle)}follwing:')
    for x in my_vehicle:
        x.vehicle_detail()
        print("\n")


# option
def display_option():
    select = 0
    print("Welcome to Vehicle Data Store System (VDSS)")
    print("1.Add Vehicle ")
    print("2.Display all Vehicle")
    print("3.exit")
    select= int(input("select(1-3)? : "))
    if select == 1:
        input_Vehicle()
    elif select==2:
        display_Vehicle()
    elif select==3:
        print("thank you.")
        exit(0)
    else:
        print("Please, select number 1-3.")



#input data
def input_Vehicle():
    brand = input("Enter Vehicle brand : ")
    model = input("Enter Vehicle model : ")
    color = input("Enter Vehicle color : ")
    maxspeed = int (input("Enter Vehicle max speed : "))
    price = float (input("Enter Vehicle price : "))

    #return (brand,model,color,maxspeed,price) # return as tuple
    my_vehicle.append(Vehicle(brand,model,color,maxspeed,price))
    print("\n----------------------------------")
    print("Already add Vehicle to store.")
    print("\n----------------------------------")

my_vehicle = []
s = 0
while s == 0:
    display_option()

#vm = input_vehicle_data()
#print(vm)
#print(type(vm))

#v1 = Vehicle(vm[0],vm[1],vm[2],vm[3],vm[4])
#v1.vehicle_detail()

#vm = input_Vehivle_data()
#v2 = Vehicle(vm[0],vm[1],vm[2],vm[3],vm[4])
#v2.my_Vehicle_detail()
#v1 = Vehicle(brand,model,color,maxspeed,price)
#v1.Vehicle_detail()
