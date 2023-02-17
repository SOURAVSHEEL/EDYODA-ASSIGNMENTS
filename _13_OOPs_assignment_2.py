## IMPLEMENT A CALCULATOR CLASS

class Calculator:

    def __init__(self):
        self.num1 = int(input("Enter first number: "))
        self.num2 = int(input("Enter second number: "))

    def add(self):
        print(self.num1 + self.num2)

    def subtract(self):
        print(self.num1 - self.num2)

    def multiply(self):
        print(self.num1 * self.num2)

    def divide(self):
        print(self.num1 / self.num2)

calculator = Calculator()
calculator.add()
calculator.subtract()
calculator.multiply()
calculator.divide()

