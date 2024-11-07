class Dog:
    def __init__(self, name, color, awake=True):
        print("Initializing a Dog object")
        self.name = name
        self.color = color
        self.awake = awake

    def __del__(self):
        print(f"Destroying a Dog object named: {self.name}")

    def bark(self):
        print(f"{self.name} => Woof! Woof!")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join(f'{key}={value}' for key, value in self.__dict__.items())}"

def create_dog():
    c_function = Dog("Zoe", "black", False)
    print(c_function)
    c_function.bark()

c = Dog("Fido", "brown")
print(c)
c.bark()

create_dog()

print("End of the program")
del c
print("End of the program")
print("End of the program")
print("End of the program")
print("End of the program")
