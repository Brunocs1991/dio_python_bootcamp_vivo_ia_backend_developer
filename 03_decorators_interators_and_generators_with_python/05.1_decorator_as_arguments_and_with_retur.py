import functools


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result

    return wrapper


@my_decorator
def say_hello(name):
    print(f"Hello {name}!")
    return name.upper()


hello = say_hello('John')
print(hello)
print(say_hello.__name__)
