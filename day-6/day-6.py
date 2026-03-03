# Day 6: Trash Compactor
# Math work sheet with 2d representation for easy retrieval.
# Columns of numbers are iterated on and the arithmetic operation applied.
# Totals from each column are then added together and returned.

import math
from fileinput import FileInput

MATH_OPS = ["*", "+"]


def construct_worksheet(file_input):
    worksheet = []
    for row_index, line in enumerate(input):
        worksheet.append([])
        # Extract just the numbers from the current line
        math_items = line.split()
        
        # Extra protection if we miss the operation row somehow
        if math_items == []:
            # Last row in the file, exit early
            break
        
        # If we are on the arthimetic operations row, don't int-ify
        if math_items[0] in MATH_OPS:
            for operation in math_items:
                worksheet[row_index].append(operation)
            break

        for number in math_items:
            worksheet[row_index].append(int(number))
    
    return worksheet


def calculate_totals(worksheet):
    totals = 0
    
    # Store the operation row for later use
    ops_row = len(worksheet) - 1

    # Use the first row to figure out the number of columns
    for col, _ in enumerate(worksheet[0]):
        col_total = 0
        
        # Find the total for the column by apply operation
        operation = worksheet[ops_row][col]
        current_row = ops_row
        col_numbers = []

        # Find all the numbers for the current column
        while True:
            # We have reached the top if we are less than 0
            if current_row == 0:
                break
            current_row = current_row - 1
            col_numbers.append(worksheet[current_row][col])

        print(operation, col_numbers)
        # Note: These arithmetic operations can be in any order
        if operation == "*":
            col_total = math.prod(col_numbers)
        elif operation == "+":
            col_total = math.fsum(col_numbers)
        print(col_total)
        totals = totals + col_total
    return int(totals)


with FileInput("input.txt") as input:
    worksheet = construct_worksheet(input)   
    print(worksheet)
    totals = calculate_totals(worksheet)
    print(totals)
