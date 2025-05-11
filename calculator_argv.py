import sys
from calculator_functions import *

'''
Calculator Through command-line arguments

E.g., Addition -> add number1 number 2
            
available args add, sub, mul, div, mod, pow
'''

def display(result):
    print(result[0])

def arg_calculate(fun, num1:float, num2:float):
    fun = str(fun).lower()

    if fun == 'add':
        return add(num1, num2)
    
    elif fun == 'sub':
        return sub(num1, num2)
    
    elif fun == 'mul':
        return mul(num1, num2)
    
    elif fun == 'div':
        if num2 == 0:
            raise ZeroDivisionError("You tried to divide by zero!")
        else:
            return div(num1, num2)

    elif fun == 'mod':
        if num2 == 0:
            raise ZeroDivisionError("You tried to divide by zero!")
        else:
            return mod(num1, num2)
    
    elif fun == 'pow':
        return pow(num1, num2)
    
    else:
        raise ValueError("Invalid operation. Use add, sub, mul, div, mod, or pow.")


def calculator():
    try:
        if len(sys.argv) != 4:
            raise ValueError("Usage: <operation> <num1> <num2>")

        fun, num1, num2 = sys.argv[1], float(sys.argv[2]),float(sys.argv[3])
        result = arg_calculate(fun, num1, num2)
        display(result)

    except ZeroDivisionError as zde:
        print(zde)
    except ValueError as ve:
        print(ve)



calculator()



