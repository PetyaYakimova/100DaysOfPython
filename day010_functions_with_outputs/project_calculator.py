def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculator():
    num1 = float(input("What is the first number? "))

    should_accumulate = True
    while should_accumulate:
        for key in operations:
            print(key)
        operation = input("Pick an operation: ")
        num2 = float(input("What is the second number? "))
        result = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n', to start a new calculation. ")

        if choice == 'y':
            num1 = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()
