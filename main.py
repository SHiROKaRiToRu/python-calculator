# Function to take input
def input_function():
    a = input("Enter first value: ")    
    b = input("Enter second value: ")

    try:                                           # ValueError handling
        return float(a), float(b)
    except ValueError:
        print("Please enter valid numbers for this operation")
        return None

# Function to perform addition
def add():
    values = input_function()
    if values is None:
        return None
    a, b = values
    return a+b

# Function to perform subtraction
def subtract():
    values = input_function()
    if values is None:
        return None
    a, b = values
    return a-b

# Function to perform multiplication
def multiply():
    values = input_function()
    if values is None:
        return None
    a, b = values
    return a*b

# Function to perform division
def divide():
    values = input_function()
    if values is None:
        return None
    a, b = values

    try:                                            #ZeroDivisionError Handling
        return a/b
    except ZeroDivisionError:
        print("Cannot divide by zero!!!")

# Function to perform modulus
def mod():
    values = input_function()
    if values is None:
        return None
    a, b = values

    return a % b

# Function to perform percentage
def percentage():
    values = input_function()
    if values is None:
        return None
    a, b = values

    return (a * b) / 100

# Function to perform exponents
def power():
    values = input_function()
    if values is None:
        return None
    a, b = values

    return a ** b

# Display menu and operation selection
def select_operation():

    choice_map = {
            1: ("Addition", add),
            2: ("Subtraction", subtract),
            3: ("Multiplication", multiply),
            4: ("Division", divide),
            5: ("Modulus", mod),
            6: ("Percentage", percentage),
            7: ("Power", power)
        }
    for key, (name, _) in choice_map.items():
        print(f"{key}.{name}")
    print("Select your operation")

    
    print("Enter 1, 2 ,3 ,4, 5, 6, 7: ")

    try:
        usr_input = int(input())
        if usr_input in choice_map:
            operation_function = choice_map[usr_input][1]
            return operation_function()
        else:
            print("Please enter a number between 1 and 6")
    except ValueError:
        print("Please enter a number between 1 and 6")
        return None
        
    

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




    
