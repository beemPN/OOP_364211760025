"""
Name: {pannika nareeloed}
SID: {364211760025}
Group: {MIT221}
"""
"""
OOP Exercise Chapter 6

1. จงเขียนโปรแกรมภาษาไพธอนเพื่อสร้างคลาสพาหนะชื่อ Vehicle ที่ประกอบไปด้วยคุณลักษณะ (attributes) คือ 
ยี่ห้อรถ (brand) 
รุ่นรถ (model)
สีรถ (color)
ความเร็วสูงสุด (max speed)
ราคา (price)

2.จากข้อที่ 1 เขียนโปรแกรมเพื่อสร้างวัตถุ (object) จากคลาส Vehicle โดยรับข้อมูลจากผู้ใช้ตามคุณลักษณะ (attributes)ของคลาส
จากนั้นแสดงข้อมูลทางหน้าจอภาพ

15 นาที;/;
"""

class Vehicle:

    def __init__(self,brand,model,color,max_speed,price):
        # object attributes
        self.brand = brand
        self.model = model
        self.color = color
        self.max_speed = max_speed
        self.price = price

    brand = input("ยี่ห้อรถ: ")
    model = input("รุ่นรถ: ")
    color = input("สีรถ: ")
    max_speed = input("ความเร็วสูงสุด: ")
    price = int(input("ราคา: "))
    print('********************')
    print('ยี่ห้อ:',brand)
    print('รุ่นรถ:',model)
    print('สีรถ:',color)
    print('ความเร็วสูงสุด:',max_speed)
    print('ราคา:',price,'บาท')
    print('********************')



