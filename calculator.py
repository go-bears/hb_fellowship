"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *



# Your code goes here
while True:
    #take in and parse user input
    try:
        input = raw_input("Enter a value: ")
        tokens = input.split(" ")
        if tokens[0] == 'q' or tokens[0]=="Q":
            break

        if len(tokens) < 2:
            command = tokens[0]
            print "You have too few numbers in a command." 


        if len(tokens) == 3:
            command = tokens[0]
            num1 = int(tokens[1])
            num2 = int(tokens[2])
        elif len(tokens) == 2:
            two_items = True
            command = tokens[0]
            num1 = int(tokens[1])
                
    except ValueError:
        print "TypeError, This isn't a number, please enter a valid number"
        # raise Exception("TypeError, This isn't a number, please enter a valid number")
        
    
    #checks input for valid calculator commands    
    commands_list = ["+", "-", "*", "/", "square", "cube", "pow", "mod"]
    if command in commands_list:
        pass
    
    else:
        raise Exception("That was not a valid calculator command. Please try again.")
        continue

    #calculates operations for two numbers
    if len(tokens) == 3:    
        if command == '+':
            print add(int(num1), int(num2))
        elif command == '-':
            print subtract(int(num1), int(num2))
        elif command == "*":
            print multiply(int(num1), int(num2))
        elif command == '/':
            print divide(float(num1), float(num2))
        elif command == 'pow':
            print power(float(num1), float(num2)) 
        elif command == 'mod':
            print mod(int(num1), int(num2))

    #operations for one number
    if len(tokens) == 2:
        if command == "square":
            print square(int(num1))
        elif command == "cube":
            print cube(int(num1))

    #error message for too many numbers        
    if len(tokens) > 3:
        print "You entered too many numbers, please try again."

    
# No setup
# repeat forever:
#     read input
#     tokenize input
#     if the first token is 'q', quit
#     otherwise decide which math function to call based on the tokens we read