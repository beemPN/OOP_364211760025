"""
Name :pannika nareeloed
ID: 364211760025
Group: MIT221
"""
class labtop:
    def __init__ (self,brand,model,cpu,ram,display,storage,price):
    # attributes
        self.__brand = brand
        self.__model = model
        self.__cpu = cpu
        self.__ram = ram
        self.__display = display
        self.__storage = storage
        self.__price = price
#getter and setter
    def get_brand (self):
        return self.__brand
    def set_brand (self,brand ):
        self.__brand = brand

    def get_model(self):
        return self.__model
    def set_name(self,model):
        self.__model = model

    def get_cpu(self):
        return self.__cpu
    def set_cpu(self,cpu):
        self.__cpu = cpu

    def get_ram(self):
        return self.__ram
    def set_ram(self,ram):
        self.__ram = ram

    def get_display (self):
        return self.__display
    def set_display (self,display ):
        self.__display = display

    def get_storage (self):
        return self.__storage
    def set_storage (self,storage ):
        self.__storage = storage

    def get_price(self):
        return self.__price
    def set_price (self,price):
        self.__price = price

    def __str__(self):
        print(f'brand:{self.__brand} Model: { self.__model}cpu: { self.__cpu}ram: { self.__ram}display:'
              f' { self.__display}storage: { self.__storage}price: { self.__price}')

s = labtop("Asus","Vivoobook 15X","Inter core i512500H",8,15.6,512,27.998)
s.__str__()

