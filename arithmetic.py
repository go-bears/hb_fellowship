def add(num1, num2):
<<<<<<< HEAD
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    # Need to turn at least argument to float for division to
    # not be integer division
    return float(num1) / float(num2) 


def square(num1):
    # Needs only one argument
    return num1 * num1


def cube(num1):
    # Needs only one argument
    return num1 * num1 * num1


def power(num1, num2):
    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
=======
    """adds two number together"""
    return num1 + num2

def subtract(num1, num2):
    """subtracts one number from another"""
    return num1 - num2

def multiply(num1, num2):
    """return product of two multiplied numbers"""
    return num1 * num2          

def divide(num1, num2):
    """returns a value on divided numbers"""
    return float(num1) / num2

def square(num1):
    """return product a number squared"""
    return num1 * num1

def cube(num1):
    """returns a value in power 3"""
    return num1 * num1 * num1

def power(num1, num2):
    """ returns product of num1 with exponent num2"""
    return num1 ** num2

def mod(num1, num2):
    """returns a remainder"""
>>>>>>> 0d0ef697c41dd5221c3f551572ac9e09a04c0479
    return num1 % num2
