"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    #take in user input
    input = raw_input("> ")
    
    #tokenize input
    tokens = input.split(" ")
    
    # quit command
    if tokens[0] == 'q' or tokens[0]=="Q":
        break

    #operations for two numbers
    if len(tokens) == 3:
        command, num1, num2 = tokens
        
        if command == '+':
            print add(int(num1), int(num2))
        elif command == '-':
            print subtract(int(num1), int(num2))
        elif command == "*":
            print multiply(int(num1), int(num2))
        elif command == '/':
            print divide(float(num1), float(num2))
        elif command == 'pow':
            print power(int(num1), int(num2)) 
        elif command == 'mod':
            print mod(int(num1), int(num2))

    #operations for one number
    elif len(tokens) == 2:
        command, num1 = tokens
        if command == "square":
            print square(int(num1))
        elif command == "cube":
            print cube(int(num1))

    
# No setup
# repeat forever:
#     read input
#     tokenize input
#     if the first token is 'q', quit
#     otherwise decide which math function to call based on the tokens we read