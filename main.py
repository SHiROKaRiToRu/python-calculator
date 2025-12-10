# Function to take input
def input_function():
    a = input("Enter first value: ")    
    b = input("Enter second value: ")

    try:                                           # ValueError handling
        a_float = float(a)
        b_float = float(b)
        return a_float, b_float
    except ValueError:
        print("Please enter valid numbers for this operation")

# Function to perform addition
def add():
    a, b = input_function()
    return a+b

# Function to perform subtraction
def subtract():
    a, b = input_function()
    return a-b

# Function to perform multiplication
def multiply():
    a, b = input_function()
    return a*b

# Function to perform division
def divide():
    a, b = input_function()

    try:                                            #ZeroDivisionError Handling
        return a/b
    except ZeroDivisionError:
        print("Cannot divide by zero!!!")

# Function to perform modulus
def mod():
    a, b = input_function()

    return a % b

# Function perform percentage
def percentage():
    a, b = input_function()

    return (a * b) / 100

# Display menu and operation selection
def select_operation():

    print("Select your operation")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("Enter 1, 2 ,3 ,4, 5, 6: ")

    try:
        usr_input = int(input())
    except ValueError:
        print("Please enter a number between 1 and 6")
        return None

    if usr_input == 1:
        return add()
    elif usr_input == 2:
        return subtract()
    elif usr_input == 3:
        return multiply()
    elif usr_input == 4:
        return  divide()
    elif usr_input == 5:
        return mod()
    elif usr_input == 6:
        return percentage()
    else:
        print("Please enter a within num 1 to 4")

# main prgram loop
while True:
    print("--- Welcome to basic Python Calculator ---")
    result = select_operation()

    if result != None:                          #None result handling
        if result.is_integer():
            result = int(result)                #Converting float to int if whole number              
            print("Result: ", result)
    again = input("Do you want to continue? (y/n): ")

    if again.lower() == 'n':
        print("Goodbye!")
        break




    
