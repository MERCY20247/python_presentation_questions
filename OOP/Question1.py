#1) Create a class called car with attributes brand and color. Instantiate an object of the Car class
#  and print it's attributes
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
my_car = Car("Nissan", "red")
print(my_car.brand) 
print(my_car.color) 
