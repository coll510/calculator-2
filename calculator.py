"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import add

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
            break
        if operator == '+':
                print(add(num1, num2))

        #elif tokens[0] == '-':   

calculator()