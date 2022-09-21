"""
Name :pannika nareeloed
ID: 364211760025
Group: MIT221
"""

class Student :
    def __init__(self,name,id):
        # attributes
        self.name = name  #public member
        self.__id = id    #private member
    def __str__(self):
        print(f'name:{self.name} ID: { self.__id}')

std = Student("Puriwiat","001")
#direct access
print(std.name, std.id)
std.__str__()

std.name = "Nattapong" # change data attribute
std.__str__()

std.id = "002"
std.__str__()

#name mangling
print(std._Student__id)

std.Student__id=="002"
std.__str__()

