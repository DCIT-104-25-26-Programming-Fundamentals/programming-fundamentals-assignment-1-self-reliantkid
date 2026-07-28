# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def addition(n1, n2):
    result = n1 + n2
    print(f"Result: {n1} + {n2} = {result}\n\n")


def subtraction(n1, n2):
    result = n1 - n2
    print(f"Result: {n1} - {n2} = {result}\n\n")


def multiplication(n1, n2):
    result = n1 * n2
    print(f"Result: {n1} * {n2} = {result}\n\n")


def division(n1, n2):
    try:
        result = n1/n2
        print(f"Result: {n1} / {n2} = {result:.2f}\n\n")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.\n\n")


def modulus(n1, n2):
    try:
        result = n1 % n2
        print(f"Result: {n1} % {n2} = {result}\n\n")
    except ZeroDivisionError:
        print("Error: Cannot perform modulus by zero.\n\n")


def expo(n1, n2):
    result = n1 ** n2
    print(f"Result: {n1} ** {n2} = {result}\n\n")


def main():
    while True:
        print("============================")
        print("     SIMPLE CALCULATOR      ")
        print("============================")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exponentiation")
        print("7. Quit")

        try: 
            user_choice = int(input("\nSelect an operation (1-7): "))

            if user_choice not in range(1, 8):
                print("Option not in list!\n")
            else:
                if user_choice != 7:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))

                if user_choice == 1:
                    addition(num1, num2)
                elif user_choice == 2:
                    subtraction(num1, num2)
                elif user_choice == 3:
                    multiplication(num1, num2)
                elif user_choice == 4:
                    division(num1, num2)
                elif user_choice == 5:
                    modulus(num1, num2)
                elif user_choice == 6:
                    expo(num1, num2)
                    
                elif user_choice == 7:
                    print("Goodbye!")
                    return
                
        except ValueError:
            print("Input must be a number in the options!\n")

main()