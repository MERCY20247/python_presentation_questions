#2) Add a method called start_engine to the Car class that prints a message saying the engine of the car has started.
#  Create an instance of Car and call the method.


class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def start_engine(self):
        print(f"The engine of the {self.brand} car has started.")
my_car = Car("Nissan", "red")
my_car.start_engine()
