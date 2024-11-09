class People:

    def __init__(self, name, year_of_birth):
        self._name = name
        self._year_of_birth = year_of_birth

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        actual_year = 2024
        return actual_year - self._year_of_birth

    @age.setter
    def age(self, year_of_birth):
        self._year_of_birth = year_of_birth


people = People("John", 1980)
print(f"Name: {people.name} \t Age: {people.age}")

people.name = "Jane"
people.age = 1990
print(f"Name: {people.name} \t Age: {people.age}")


