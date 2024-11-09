class Bird:
    def fly(self):
        print("Bird can fly")


class Sparrow(Bird):
    def fly(self):
        print("Sparrow can fly")


class Ostrich(Bird):
    def fly(self):
        print("Ostrich can't fly")

# FIXME: Airplane is not a bird bad example of heritage to gain the method fly
class Airplane(Bird):
    def fly(self):
        print("Airplane can fly")


def flight_plan(obj):
    obj.fly()


flight_plan(Sparrow())
flight_plan(Ostrich())
flight_plan(Airplane())
