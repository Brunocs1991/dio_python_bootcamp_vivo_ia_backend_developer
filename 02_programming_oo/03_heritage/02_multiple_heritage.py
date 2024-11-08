class Animals:
    def __init__(self, number_of_legs):
        self.number_of_legs = number_of_legs

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join(f'{key}={value}' for key, value in self.__dict__.items())}"


class Mammals(Animals):
    def __init__(self, fur_color, **kw):
        super().__init__(**kw)
        self.fur_color = fur_color


class Birds(Animals):
    def __init__(self, beak_color, **kw):
        super().__init__(**kw)
        self.beak_color = beak_color


class Dog(Mammals):
    pass

class SpeakMixin:
    def speak(self):
        return "I am speaking"


class Platypus(Mammals, Birds, SpeakMixin):
    def __init__(self, fur_color, beak_color, number_of_legs):
        print(Platypus.__mro__)
        super().__init__(fur_color=fur_color, number_of_legs=number_of_legs, beak_color=beak_color)
        # self.beak_color = beak_color
    # pass


dog = Dog(number_of_legs=4, fur_color="brown")
print(dog)

platypus = Platypus(number_of_legs=4, fur_color="red", beak_color="yellow")
print(platypus.speak())
print(platypus)
