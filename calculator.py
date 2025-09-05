"""
TASK: Create a Calculator class.

Requirements:
1. The class should allow basic operations: add, subtract, multiply, divide.
2. Each operation should be a separate method.
3. Handle division by zero gracefully.
4. Allow both integers and floats.

Example Usage:
    calc = Calculator()
    print(calc.add(5, 3))        # 8
    print(calc.divide(10, 0))    # "Error: Division by zero"
"""
class Calculator:
    def __init__(self, num1, num2): #multiply, divide):
        self.num1 = num1
        self.num2 = num2
        #self.multiply = multiply
        #self.divide = divide

    #add
    def add(self):
        return self.num2 + self.num1

    #subtract
    def subtract(self):
        return self.num1 - self.num2

    #multiplication
    def multiply(self):
        mul = num1 * num2
        return mul

    #division
    def divide(self):
        if num2 == 0:
            return f"Invalid operation, cannot divide by zero"
        else:
            return num1 / num2

        
num1 = float(input("Enter number: "))
num2 = float(input("Enter second number: "))

addition = Calculator(num1, num2)
subtraction = Calculator(num1, num2)
multiplication = Calculator(num1, num2)
division = Calculator(num1, num2)
print(addition.add())
#print(subtraction.subtract())
#print(multiplication.multiply())
print(division.divide())







