"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    #take in user input
    try:
    #if type(num1) and type(num2) == "int" or type(num1) and type(num2) == "float":
        input = raw_input("Enter a value: ")
        tokens = input.split(" ")
        if len(tokens) == 3:
            command = tokens[0]
            num1 = int(tokens[1])
            num2 = int(tokens[2])
        elif len(tokens) == 2:
            command = tokens[0]
            num1 = int(tokens[1])
        # else:
        #     raise Exception("You entered too many numbers, please try again.")


        
    except:
        raise Exception("TypeError, This isn't a number, please enter a valid number")
        continue
        

    
    #tokenize input
    
    # quit command
    if tokens[0] == 'q' or tokens[0]=="Q":
        break


    # #operations for two numbers
    # if len(tokens) == 3:
    #     command, num1, num2 = tokens
        
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