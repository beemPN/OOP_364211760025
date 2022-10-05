
"""
Name :pannika nareeloed
ID: 364211760025
Group: MIT221
"""
#from Mid_Exam.evcar_append import brand

class Ev_Car:
    #class attribute
    my_Ev_Car = []
def __init__(self,Brand,Model,Horsepower,Batterysize,Range,Price):
    self.Brand = Brand
    self.Model = Model
    self.Horsepower = Horsepower
    self.Batterysize = Batterysize
    self.Range = Range
    self.Price = Price

def evcar_detail(self):
        print(f'Brand:{self.Brand} '
              f'Model:{self.Model} '
              f'Color:{self.Horsepower} '
              f'Batterysize:{self.Batterysize} '
              f'Range:{self.Range} '
              f'Price:{self.Price}')
