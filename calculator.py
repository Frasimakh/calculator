from sys import exit


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Division by zero!")
        exit()


first_number = float(input("First number: "))
second_number = float(input("Second number: "))
operation = input("Enter an operation (+,-,*,/) : ")

calculations = {
    "+": addition(first_number, second_number),
    "-": subtraction(first_number, second_number),
    "*": multiplication(first_number, second_number),
    "/": division(first_number, second_number)
}

print("Result: {}".format(calculations[operation]))