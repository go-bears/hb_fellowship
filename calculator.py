"""
calculator.py

Uses our arithmetic.py file, create the
calculator program REPL.
"""

from arithmetic import *


# Your code goes here

def parse_input(input):
    """tokenizes user input, outputs command, number_list"""

    tokens = input.split(" ")
    command = tokens[0]
    number_list = tokens[1:]
    tokenized_input = command, number_list
    
    return tokenized_input

def quit_calculator(tokenized_input): 
    """checks for quit command"""
    command, number_list = tokenized_input
    if command == 'q' or command=="Q":
        return False

def validates_number_input(tokenized_input):
    """checks input for valid numbers"""
    command, number_list = tokenized_input
    
    try:
        valid_num_list= [int(i) for i in number_list]
        
        return valid_num_list

    except ValueError:
        print "TypeError, This isn't a number, please enter a valid number"

    try:
        valid_num_list = [float(i) for i in number_list]
        tokenized_input = command, float_list
        return valid_num_list

    except ValueError:
        print "TypeError, This isn't a number, please enter a valid number"

    return valid_num_list


def validates_commands(tokenized_input):
    """checks input for valid calculator commands"""
    command, number_list = tokenized_input
    try:        
        commands_list = ["+", "-", "*", "/", "square", "cube", "pow", "mod"]
        if command in commands_list:
            return command    
    except:
        print Exception("That was not a valid calculator command. Please try again.")

    return command
    

def calculator_operations(calc_input):
    """performs math operations with imported methods from arithmetic.py"""
    command, valid_num_list = calc_input

    if command == '+':
        result = reduce(lambda num1, num2: add(num1, num2), valid_num_list) 
        return result
    elif command == '-':
        result = reduce(lambda num1, num2: subtract(num1, num2), valid_num_list)
        return result
    elif command == "*":
        result = reduce(lambda num1, num2: multiply(num1, num2), valid_num_list)
        return result
    elif command == '/':
        result = reduce(lambda num1, num2: divide(num1, num2), valid_num_list)
        return result

    elif command == 'pow':        
        result = reduce(lambda num1, num2: power(num1, num2), valid_num_list)
        return result
    elif command == 'mod':
        result = reduce(lambda num1, num2: mod(num1, num2), valid_num_list)
        return result

    #operations for one number; uses reduce function to reduce number_list to a single value
    if command == "square":
        result = reduce(lambda num1, num2: add(num1, num2), valid_num_list)
        return square(result)
        
    elif command == "cube":
        result = reduce(lambda num1, num2: add(num1, num2), valid_num_list)
        return cube(result)

def main():
    while True:
        input = raw_input(">> ")
        tokenized_input = parse_input(input)
        quit_calculator(tokenized_input)
        valid_num_list = validates_number_input(tokenized_input)
        command = validates_commands(tokenized_input)
        calc_input = command, valid_num_list
        print calculator_operations(calc_input)

main()
