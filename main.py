def add():
    a = float(input("Enter first value: "))
    b = float(input("Enter second value: "))

    return a+b

def subtract():
    a = float(input("Enter first value: "))
    b = float(input("Enter second value: "))

    return a-b

def multiply():
    a = float(input("Enter first value: "))
    b = float(input("Enter second value: "))

    return a*b

def divide():
    a = float(input("Enter first value: "))
    b = float(input("Enter second value: "))

    return a / b



def select_operation():

    print("Select your operation")

    print("1. Addition")
    print("2. Substraction")
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

while True:
    print("--- Welcome to basic Python Calculator ---")
    result = select_operation()
    print("Result: ", result)
    again = input("Do you want to continue? (y/n): ")

    if again.lower() == 'n':
        print("Goodbye!")
        break




    
