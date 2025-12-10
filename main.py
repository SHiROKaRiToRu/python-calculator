# Function to perform addition
def add():
    a = input("Enter first value: ")
    b = input("Enter second value: ")

    try:                                           # ValueError handling
        a_float = float(a)
        b_float = float(b)
        return a_float +b_float
    except ValueError:
        print("Please enter valid numbers for this operation")

# Function to perform subtraction
def subtract():
    a = input("Enter first value: ")
    b = input("Enter second value: ")

    try:                                           # ValueError handling
        a_float = float(a)
        b_float = float(b)
        return a_float - b_float
    except ValueError:
        print("Please enter valid numbers for this operation")

# Function to perform multiplication
def multiply():
    a = input("Enter first value: ")
    b = input("Enter second value: ")

    try:                                           # ValueError handling
        a_float = float(a)
        b_float = float(b)
        return a_float * b_float
    except ValueError:
        print("Please enter valid numbers for this operation")

# Function to perform division
def divide():
    a = input("Enter first value: ")
    b = input("Enter second value: ")

    try:                                           # ValueError handling & ZeroDivisionError
        a_float = float(a)
        b_float = float(b)
        return a_float / b_float
    except ValueError:
        print("Please enter valid numbers for this operation")
    except ZeroDivisionError:
        print("Cannot divide by zero!!!")


# Display menu and operation selection
def select_operation():

    print("Select your operation")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("Enter 1, 2 ,3 ,4 :")

    usr_input = int(input())

    if usr_input == 1:
        return add()
    elif usr_input == 2:
        return subtract()
    elif usr_input == 3:
        return multiply()
    elif usr_input == 4:
        return  divide()
    else:
        print("Please enter a within num 1 to 4")

# main prgram loop
while True:
    print("--- Welcome to basic Python Calculator ---")
    result = select_operation()

    if result != None:                              #None result handling
        print("Result: ", result)
    again = input("Do you want to continue? (y/n): ")

    if again.lower() == 'n':
        print("Goodbye!")
        break




    
