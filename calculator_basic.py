from calculator_functions import * 
import sys
import os

def get_operator():
    return input("""
Hello Welcome to Basic Calculator  
--------------------------------
Select your option  
    1 - Addition      2 - Subtraction   3 - Multiplication  
    4 - Division      5 - MOD           6 - POWER  
    Q - Quit          R - Restart
(Enter your choice E.g., if Addition type 1) : """)

def get_operands():
    num1 = float(input("    Enter first Number  : "))
    num2 = float(input("    Enter second Number : "))
    
    return num1, num2

def exit_calculator():
    sys.exit()
        
def calculate(operator, num1, num2):    
    if operator ==  '1':
        return add(num1,num2)

    elif operator ==  '2':
        return sub(num1,num2)
        
    elif operator ==  '3':
        return mul(num1,num2)
        
    elif operator ==  '4':
        return div(num1,num2)
        
    elif operator ==  '5':
        return mod(num1,num2)
        
    elif operator ==  '6':
        return pow(num1,num2)
        
    else:
        print("Valid input please\n")

def print_red_msg(msg, err= None):
    #ANSI Colors
    # \033[91m starts red color
    # \033[0m resets to normal text
    print(f"\033[91m{msg} - {err}\033[0m\n")

def print_yellow_msg(msg):
    #ANSI Colors
    # \033[93m starts yellow color
    # \033[0m resets to normal text
    print(f"\033[93m{msg}\033[0m\n")


def calculator():
        try:
            operator = get_operator()
            if operator.lower() == 'q':    
                print("Thank you, Good bye\n")
                sys.exit()

            elif operator.lower() == 'r':
                print("restarting...\n")
                os.system('clear')
                return
            
            elif int(operator) > 0 and int(operator) <= 6:

                num1, num2 = get_operands()

                result = calculate(operator, num1, num2)
                
                print_yellow_msg(f"""
    output: {num1} {result[1]} {num2}
          = {result[0]}
""")
            else:
                print_red_msg("\nPlease check your input and Try Again")

        except ZeroDivisionError as zde:
            print_red_msg("\nCannot Divide by Zero")
            print(zde)
        except ValueError as ve:
            print_red_msg("\nEnter Valid Inputs ",ve)
            print(ve)


while True:
     calculator()

        
    