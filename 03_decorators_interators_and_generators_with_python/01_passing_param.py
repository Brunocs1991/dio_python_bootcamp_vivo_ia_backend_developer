def message(name):
    print("executing message")
    return f'Hello {name}'

def long_message(name):
    print("executing long_message")
    return f'Hello {name}, how are you?'

def execute(func, name):
    print("executing execute")
    return func(name)

print(execute(message, 'John'))
print(execute(long_message, 'John'))
