class Student:
    school = "ABC School"

    def __init__(self, name, registration) -> None:
        self.name = name
        self.registration = registration

    def __str__(self) -> str:
        return f"{self.name} - {self.registration} - {self.school}"

def show_values(*objs) -> None:
    for obj in objs:
        print(obj)

student = Student("John", 123)
student2 = Student("Jane", 456)
show_values(student, student2)

student.registration = 789
show_values(student, student2)

Student. school = "XYZ School"
student3 = Student("Alice", 101)
show_values(student, student2, student3)
