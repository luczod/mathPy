# 4: Fraction Calculator
# Fraction operations
from fractions import Fraction


def add(a: Fraction, b: Fraction):
    print("Result of Addition: {0}".format(a + b))


def subtract(a: Fraction, b: Fraction):
    print("Result of Subtraction: {0}".format(a - b))


def divide(a: Fraction, b: Fraction):
    print("Result of Division {0} by {1}: {2}".format(a, b, (a / b)))


def multiply(a: Fraction, b: Fraction):
    print("Result of Multiplication: {0}".format(a * b))


if __name__ == "__main__":
    a = Fraction(input("Enter first fraction: "))
    b = Fraction(input("Enter second fraction: "))
    op = input("Operation to perform - Add, Subtract, Divide, Multiply: ")

    if op == "Add":
        add(a, b)

    if op == "Subtract":
        subtract(a, b)

    if op == "Divide":
        divide(a, b)

    if op == "Multiply":
        multiply(a, b)
