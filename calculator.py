"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *



# Your code goes here
while True:
    #take in and parse user input
    input = raw_input(">> ")
    tokens = input.split(" ")
    command = tokens[0]
    number_list = tokens[1:]

    #quit command
    if tokens[0] == 'q' or tokens[0]=="Q":
        break

    # float_list = []
    # for item in number_list:
    #     item = float(item)
    #     float_list.append(item)

    #checks input for valid numbers    
    try:
        number_list = [int(i) for i in number_list]

    except ValueError:
        print "TypeError, This isn't a number, please enter a valid number"

    try:
        float_list = [float(i) for i in number_list]
    except ValueError:
        print "TypeError, This isn't a number, please enter a valid number"

    
    #checks input for valid calculator commands    
    try:        
        commands_list = ["+", "-", "*", "/", "square", "cube", "pow", "mod"]
        if command in commands_list:
            pass    
    except:
        print Exception("That was not a valid calculator command. Please try again.")
        

    #calculates operations        
    if command == '+':
        result = reduce(lambda num1, num2: add(num1, num2), number_list) 
        print result

    elif command == '-':
        result = reduce(lambda num1, num2: subtract(num1, num2), number_list)
        print result
    elif command == "*":
        result = reduce(lambda num1, num2: multiply(num1, num2), number_list)
        print result
    elif command == '/':
        result = reduce(lambda num1, num2: divide(num1, num2), float_list)
        print result

    elif command == 'pow':
        result = reduce(lambda num1, num2: power(num1, num2), float_list)
        print power(float(num1), float(num2)) 
    elif command == 'mod':
        result = reduce(lambda num1, num2: mod(num1, num2), number_list)
        print result

    #operations for one number *use reduce function to reduce to single value
    if command == "square":
        result = reduce(lambda num1, num2: add(num1, num2), number_list)
        print square(result)
        
    elif command == "cube":
        result = reduce(lambda num1, num2: add(num1, num2), number_list)
        print cube(result)

 
    
# No setup
# repeat forever:
#     read input
#     tokenize input
#     if the first token is 'q', quit
#     otherwise decide which math function to call based on the tokens we read