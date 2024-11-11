def calculator(operator):
    def sum(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mul(a, b):
        return a * b

    def div(a, b):
        return a / b

    match operator:
        case '+':
            return sum
        case '-':
            return sub
        case '*':
            return mul
        case '/':
            return div

op = calculator('+')
print(op(10, 5))
op = calculator('-')
print(op(10, 5))
op = calculator('/')
print(op(10, 5))
op = calculator('*')
print(op(10, 5))
