# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def first_n_fibonacci(n):
    sequence = [0, 1]
    display_sequence = ""

    if n <= 0:
        print("Error: N must be a positive integer!")
        return
    else:
        for i in range(1, n-1):
            next_term = sequence[i] + sequence[i-1]
            sequence.append(next_term)

    for j in range(n):
        display_sequence += f"{str(sequence[j])} "

    return display_sequence


def check_fibonacci(n):
    sequence = [0, 1]
    i = 1

    if n < 0:
        print("Error: N must be a positive integer!")
        return
    else:
        while sequence[-1] < n:
            next_term = sequence[i] + sequence[i-1]
            sequence.append(next_term)
            i += 1

        if n in sequence:
            return "is"
        else:
            return "is NOT"



def main():
    n1 = int(input("How many terms? "))
    fib_sequence = first_n_fibonacci(n1)
    print("Fibonacci sequence:", fib_sequence)

    n2 = int(input("\nEnter a number to check: "))
    status = check_fibonacci(n2)
    print(f"{n2} {status} a Fibonacci number")


main()