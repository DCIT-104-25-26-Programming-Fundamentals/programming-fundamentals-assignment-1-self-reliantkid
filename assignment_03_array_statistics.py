# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def sum_function(nums):
    result = 0

    for num in nums:
        result += num

    return result


def average_function(nums):
    num_sum = sum_function(nums)
    result = num_sum/len(nums)
    return result


def max_function(nums):
    result = nums[0]

    for num in nums:
        if num > result:
            result = num

    return result


def min_function(nums):
    result = nums[0]

    for num in nums:
        if num < result:
            result = num

    return result



def main():
    nums_list = []
    num_count = int(input("How many numbers? "))
    i = 1

    while i <= num_count:
        num = int(input(f"Enter number {i}: "))

        if num <= 0:
            print("Error: Enter a number greater than 0")
            return
        else:
            nums_list.append(num)
            i += 1

    sum_result = sum_function(nums_list)
    avg_result = average_function(nums_list)
    max_result = max_function(nums_list)
    min_result = min_function(nums_list)

    print("\nResults:")
    print("Sum:", sum_result)
    print("Average:", avg_result)
    print("Max:", max_result)
    print("Min:", min_result)


main()