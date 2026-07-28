# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================



def read_matrix(rows, cols):
    matrix = []
    for i in range(1, rows + 1):
        while True:
            parts = input(f"Enter row {i}: ").split()
            if len(parts) == cols:
                matrix.append([int(x) for x in parts])
                break
            print(f"Row must have {cols} numbers.")
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print("  ".join(str(val) for val in row))

def transpose():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    matrix = read_matrix(rows, cols)
    
    result = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        result.append(new_row)
        
    print("\nTransposed Matrix:")
    print_matrix(result)

def addition():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    print("Matrix 1")
    m1 = read_matrix(rows, cols)
    print("Matrix 2")
    m2 = read_matrix(rows, cols)
    
    result = []
    for r in range(rows):
        new_row = []
        for c in range(cols):
            new_row.append(m1[r][c] + m2[r][c])
        result.append(new_row)
        
    print("\nResult:")
    print_matrix(result)

def multiplication():
    rows_a = int(input("Enter rows for Matrix A: "))
    cols_a = int(input("Enter columns for Matrix A: "))
    rows_b = int(input("Enter rows for Matrix B: "))
    cols_b = int(input("Enter columns for Matrix B: "))
    
    if cols_a != rows_b:
        print("Cannot multiply: columns of A must equal rows of B.")
        return
        
    print("Matrix A")
    a = read_matrix(rows_a, cols_a)
    print("Matrix B")
    b = read_matrix(rows_b, cols_b)
    
    result = []
    for i in range(rows_a):
        new_row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += a[i][k] * b[k][j]
            new_row.append(total)
        result.append(new_row)
        
    print("\nResult:")
    print_matrix(result)

def main():
    print("Part A - Transpose")
    transpose()
    print("\nPart B - Addition")
    addition()
    print("\nPart C - Multiplication")
    multiplication()

main()