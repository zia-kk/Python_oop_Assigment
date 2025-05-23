#Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    def __init__(self , barand:str):
        self.brand=barand
    def start(self):
        print(f"{self.brand} is Starting....")

if __name__ == "__main__":

     My_car= Car("Suzuki")

     print(My_car.brand)

     My_car.start()
        