class Vehicle:

    def __init__(self, color, plate, number_for_wheels):
        self.color = color
        self.plate = plate
        self.number_for_wheels = number_for_wheels

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join(f'{key}={value}' for key, value in self.__dict__.items())}"

    def start_engine(self):
        print("Starting engine")

class Motorcycle(Vehicle):
    pass

class Car(Vehicle):
    pass

class Truck(Vehicle):
    def __init__(self, color, plate, number_for_wheels, charger):
        super().__init__(color, plate, number_for_wheels)
        self.chager = charger

    def this_charger(self):
        print(f"Charging the truck: {self.chager}")
    pass

motorcycle = Motorcycle("red", "1234", 2)
motorcycle.start_engine()
print(motorcycle)

car = Car("blue", "5678", 4)
car.start_engine()
print(car)

truck = Truck("green", "9012", 6, False)
truck.start_engine()
truck.this_charger()
print(truck)
