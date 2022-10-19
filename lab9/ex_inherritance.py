"""
Name :pannika nareeloed
ID: 364211760025
Group: MIT221
"""

# class Relation - Inherritance

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def person_info(self):
        print(f'Name: {self.name} Age: {self.age}')

class Student(Person):
    def __init__(self,name,age,major,gpa):
        # 1
        Person.__init__(self,name,age)
       #super(Student, self).()
        self.major = major
        self.gpa = gpa
    def student_info(self):
        self.person_info()
        print(f'Major: {self.major} Gpa: {self.gpa}')


# class object
p1 = Person("Puriwat",36)
s1 = Student("mint",22,"MIT",3.50)

p1.person_info()
s1.person_info()

s1.student_info()