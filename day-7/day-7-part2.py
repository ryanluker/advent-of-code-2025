# Day 7 Part 2: Laboratories
# Many worlds beam printer
#
# Tactics:
# - Leverage depth first search pattern
# - Print each manifold state once reached the bottom
# - Recursively traverse the beam splitter tree

from functools import cache
from time import sleep
from fileinput import FileInput


def traverse_beam_array(current_state_beam_array, row, column):
    # Reached the bottom of the beam path, bubble up a value of 1
    if len(current_state_beam_array) == row + 2:
        return 1
    
    current_value = current_state_beam_array[row][column]
    current_below_value = current_state_beam_array[row + 1][column]

    # Nothing below (or at start), continue beam traversal
    if (current_value == "|" or current_value == "S") and current_below_value == ".":
        current_state_beam_array[row + 1][column] = "|"
        unique_beam_count = traverse_beam_array(current_state_beam_array, row + 1, column)
        # Return up the stack with the accumulated beam count
        current_state_beam_array[row + 1][column] = "."
        return unique_beam_count

    # Splitter below, split the beam
    if current_value == "|" and current_below_value == "^":
        current_state_beam_array[row + 1][column - 1] = "|"
        unique_beam_count_left = traverse_beam_array(current_state_beam_array, row + 1, column - 1)
        # Unset the beam as we are heading back up the call stack
        current_state_beam_array[row + 1][column - 1] = "."
        current_state_beam_array[row + 1][column + 1] = "|"
        unique_beam_count_right = traverse_beam_array(current_state_beam_array, row + 1, column + 1)
        # Unset the beam as we are heading back up the call stack
        current_state_beam_array[row + 1][column + 1] = "."
        unique_beam_count = unique_beam_count_left + unique_beam_count_right
        current_state_beam_array[row + 1][column] = unique_beam_count
        return unique_beam_count

    # Found a cached subgraph, increment and return
    if current_value == "|" and type(current_below_value) == int:
        return current_below_value


def load_manifold(file_input):
    manifold = []
    starting_column = 0
    for row, line in enumerate(file_input):
        striped_line = line.strip()
        manifold.append([])
        for column, char in enumerate(striped_line):
            # By default, append the character to the beam layout.
            manifold[row].append(char)
            if char == "S":
                starting_column = column

    return manifold, starting_column


def print_manifold_state(manifold_layout):
    """Pretty prints the manifold layout for human visualization."""
    for line in manifold_layout:
        fmt_line = [
            str(value)
            for value in line
        ]
        print("".join(fmt_line))


with FileInput("input.txt") as file_input:
    starting_manifold, starting_column = load_manifold(file_input)
    final_count = traverse_beam_array(starting_manifold, 0, starting_column)
    print_manifold_state(starting_manifold)
    print(final_count)
