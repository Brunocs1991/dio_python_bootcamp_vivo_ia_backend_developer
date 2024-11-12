def my_generator(numbers: list[int]):
    for number in numbers:
        yield number * 2

for i in my_generator([1, 2, 3]):
    print(i)
