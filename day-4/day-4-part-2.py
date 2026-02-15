# Day 4: Printing Department Part 2
# Mostly the same as part 1 but we must also iterate til no rolls are removed

import copy
from time import sleep
from fileinput import FileInput


def render_warehouse(warehouse):
    for row in warehouse:
        print("".join(row))


def generate_warehouse_map(input):
    """Takes an input and loads it into a 2d array"""
    warehouse_map = []
    for row, warehouse_row in enumerate(input):
        if warehouse_row == "\n":
            break
        # Setup the next row of the warehouse
        warehouse_map.append([])
        for roll in warehouse_row:
            if roll == "\n":
                break
            warehouse_map[row].append(roll)
    return warehouse_map


def count_nearby_rolls(row, column, warehouse):
    """
    Figures out the number of nearby rolls in the 8 cardinal directions
    @@@
    @X@
    @@@

    We always count from the center, so we ignore this position.
    """
    def safe_row_select(position):
        left_bound = column - 1
        # Account for array split working different on the range end
        right_bound = column + 2
        if position == "top":
            # Check if we are above the top
            try:
                line = warehouse[row-1]
                if row-1 == -1:
                    return []
            except:
                return []

            # Check if we are at the very edges
            try:
                line[left_bound]
                if left_bound == -1:
                    return line[0:right_bound]
            except:
                return line[left_bound+1:right_bound]
            
            try:
                line[right_bound-1]
            except:
                return line[left_bound:right_bound-1]

            # If both bounds are valid, continue
            return line[left_bound:right_bound]
        elif position == "middle":
            line = warehouse[row]
            # Check if we are at the very edges
            try:
                line[left_bound]
                if left_bound == -1:
                    return line[0:right_bound]
            except:
                return line[left_bound+1:right_bound]
            
            try:
                line[right_bound-1]
            except:
                return line[left_bound:right_bound-1]

            # If both bounds are valid, continue
            return line[left_bound:right_bound]
        elif position == "bottom":
            try:
                line = warehouse[row+1]
            except:
                return []
            
            # Check if we are at the very edges
            try:
                line[left_bound]
                if left_bound == -1:
                    return line[0:right_bound]
            except:
                return line[left_bound+1:right_bound]
            
            try:
                line[right_bound-1]
            except:
                return line[left_bound:right_bound-1]

            return line[left_bound:right_bound]

    def count_row(line):
        count = 0
        for roll in line:
            if roll == "@":
                count = count + 1
        return count

    count = 0
    top_row = safe_row_select("top")
    count = count + count_row(top_row)

    middle_row = safe_row_select("middle")
    count = count + count_row(middle_row)

    bottom_row = safe_row_select("bottom")
    count = count + count_row(bottom_row)
    return count


def calculate_heatmap(warehouse):
    """Takes a warehouse and figures out the roll heatmap"""
    count = 0
    copy_warehouse = copy.deepcopy(warehouse)
    for row, content in enumerate(warehouse):
        for column, roll in enumerate(content):
            if copy_warehouse[row][column] == ".":
                # Skip calculating for this spot
                continue
            nearby_num = count_nearby_rolls(row, column, warehouse)
            # Remove the center roll from the calculation
            nearby_num = nearby_num - 1
            if nearby_num < 4:
                # Remove the roll for future iterations
                copy_warehouse[row][column] = str(".")
                count = count + 1
    return copy_warehouse, count


def loop_warehouse_mapping(warehouse, current_count):
    # Recursive loop for finding all the rolls
    new_warehouse, nearby_count = calculate_heatmap(warehouse)
    render_warehouse(new_warehouse)
    current_count = current_count + nearby_count
    # We can exit the recursive loop if we get 0
    if nearby_count == 0:
        print(f"Final count: {current_count}")
        return current_count
    # If the count was not 0 we might have more rolls to remove
    loop_warehouse_mapping(new_warehouse, current_count)


with FileInput("input.txt") as input:
    warehouse = generate_warehouse_map(input)
    render_warehouse(warehouse)
    loop_warehouse_mapping(warehouse, 0)
