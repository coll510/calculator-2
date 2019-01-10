"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

# Your code goes here
def calculator():
    while True:
        user_input = input("Please enter an operator followed by the numbers, seperate the inputs with spaces. Enter q if you would like to quit the program. " ) 
        tokens = user_input.split(" ")
        try:
            operator = tokens[0]
            num1 = int(tokens[1])
            num2 = int(tokens[2])
        except IndexError:
            if operator == 'square':
                print(square(num1))
            elif operator == 'cube':
                print(cube(num1))
            else:
                break
        if operator == '+':
                print(add(num1, num2))
        elif operator == '-':
                print(subtract(num1, num2))
        elif operator == '*':
                print(multiply(num1, num2))                
        elif operator == '/':
                print(divide(num1, num2))
        elif operator == 'pow':
                print(power(num1, num2))                
        elif operator == 'mod':
                print(mod(num1, num2))

calculator()