class MyInterator:
    def __init__(self, numbers: list[int]):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            number = self.numbers[self.index]
            self.index += 1
            return number * 2
        except IndexError:
            raise StopIteration()


for i in MyInterator(numbers=[1, 2, 3, 4, 5, 69, 55, 11]):
    print(i)
