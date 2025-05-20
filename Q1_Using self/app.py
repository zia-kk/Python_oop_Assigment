#Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

class Student:
    def __init__(self , name:str , marks:int):
        self.name=name
        self.marks=marks

x=Student("Zia" , 690)

print(x.name , x.marks)
