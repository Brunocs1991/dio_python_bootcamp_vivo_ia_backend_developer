def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_hello(name):
    print(f"Hello {name}!")


say_hello('John')
