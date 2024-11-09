class People:
    def __init__(self, name=None, age=None) -> None:
        self.name = name
        self.age = age

    @classmethod
    def create_from_date_of_birth(cls, year, month, day, name):
        age = 2024 - year
        return cls(name, age)

    @staticmethod
    def is_adult(age):
        return age >= 18

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join(f'{key}={value}' for key, value in self.__dict__.items())}"


p = People("John", 30)
print(p)

p2 = People.create_from_date_of_birth(1991, 5, 31, "Jane")
print(p2)

print(People.is_adult(p2.age))
print(People.is_adult(17))
