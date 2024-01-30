#1. Return as an early exit

def format_name(f_name, l_name):
  """Take a first and last name and format it 
  to return the title case version of the name."""
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"Result: {formated_f_name} {formated_l_name}"


#2. Days in months
# Program to calculate the number of days in a month for different years.
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]
  
    
year = int(input("Enter a year: ")) 
month = int(input("Enter a month: ")) 
days = days_in_month(year, month)
print(days)

#3. CALCULATOR PROJECT (Part 1)
# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = float(input("Enter the first number: "))

for operator in operations:
    print(operator)
operator_sign = input("Pick an operation from the operations above: ")

operator_choice = operations[operator_sign]

num2 = float(input("Enter the second number: "))
answer = operator_choice(num1, num2)

print(f"{num1} {operator_sign} {num2} = {answer}")



#4. CALCULATOR PROJECT (Part 2)
# While loop, flags and recursion

from IPython.display import clear_output

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("Enter the first number: "))

    for operator in operations:
        print(operator)

    continue_calculation = True

    while continue_calculation:
        operator_sign = input("Pick an operation from the operations above: ")

        operator_choice = operations[operator_sign]

        num2 = float(input("Enter the second number: "))
        answer = operator_choice(num1, num2)

        print(f"{num1} {operator_sign} {num2} = {answer}")

        feedback = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if feedback == "y":
            num1 = answer
        else:
            continue_calculation = False
            clear_output()
            calculator()

# Call the calculator function
calculator()


#4. CALCULATOR PROJECT (Final code)

# While loop, flags and recursion

from IPython.display import clear_output
from art import logo

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    num1 = float(input("Enter the first number: "))

    for operator in operations:
        print(operator)

    continue_calculation = True

    while continue_calculation:
        operator_sign = input("Pick an operation from the operations above: ")

        operator_choice = operations[operator_sign]

        num2 = float(input("Enter the second number: "))
        answer = operator_choice(num1, num2)

        print(f"{num1} {operator_sign} {num2} = {answer}")

        feedback = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if feedback == "y":
            num1 = answer
        else:
            continue_calculation = False
            clear_output()
            calculator()

# Call the calculator function
calculator()
