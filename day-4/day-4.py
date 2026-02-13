# Day 4: Printing Department
# Construct a heat map of nearby paper rolls
# The corrisponding 2d array should have nearby roll totals as a numeric
# Performance wise, should only need to iterate over the full "warehouse" once + 8 calculations for the directions

import copy
from fileinput import FileInput


def render_warehouse(warehouse):
    for row in warehouse:
        print(row)


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
    heatmap_warehouse = copy.deepcopy(warehouse)
    for row, content in enumerate(warehouse):
        for column, roll in enumerate(content):
            if heatmap_warehouse[row][column] == ".":
                # Skip calculating heatmap for this spot
                continue
            nearby_num = count_nearby_rolls(row, column, warehouse)
            # Remove the center roll from the calculation
            nearby_num = nearby_num - 1
            heatmap_warehouse[row][column] = str(nearby_num)
            if nearby_num < 4:
                count = count + 1
    return heatmap_warehouse, count

with FileInput("example-input.txt") as input:
    warehouse = generate_warehouse_map(input)
    render_warehouse(warehouse)
    print("-------------------------------------")
    heatmap_warehouse, nearby_count = calculate_heatmap(warehouse)
    render_warehouse(heatmap_warehouse)
    print(f"Final nearby count: {nearby_count}")
