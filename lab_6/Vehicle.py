
"""
Name :pannika nareeloed
ID: 364211760025
Group: MIT221
"""
#from lab_6.vihecle_append import brand


class Vehicle:
    #class attribute
    my_Vehicle = []
def __init__(self,brand,model,color,maxspeed,price):
    self.brand = brand
    self.model = model
    self.color = color
    self.maxspeed = maxspeed
    self.price = price
    self.my_vihecle_append(self)

    def Vehicle_detail(self):
        print(f'Brand:{self.brand} '
              f'Model:{self.model} '
              f'color:{self.color} '
              f'maxspeed:{self.maxspeed} '
              f'price:{self.price}')
