# Day 7 Part 2: Laboratories
# Many worlds beam printer
#
# Tactics:
# - Leverage depth first search pattern
# - Print each manifold state once reached the bottom
# - Recursively traverse the beam splitter tree

from time import sleep
from fileinput import FileInput

beam_count = 0


def traverse_beam_array(current_state_beam_array, row, column):
    # We have reached the bottom of the manifold for the current beam
    if len(current_state_beam_array) == row + 2:
        # Keep track of beam exits
        global beam_count
        beam_count += 1
        return

    current_array_value = current_state_beam_array[row][column]
    below_current_value = current_state_beam_array[row + 1][column]
    below_current_left_value = current_state_beam_array[row + 1][column - 1]

    # We are at S kickoff the single beam
    if current_array_value == "S" and below_current_value == ".":
        current_state_beam_array[row + 1][column] = "|"
        traverse_beam_array(current_state_beam_array, row + 1, column)

    # Continue the beam traversal
    if current_array_value == "|" and below_current_value == ".":
        current_state_beam_array[row + 1][column] = "|"
        traverse_beam_array(current_state_beam_array, row + 1, column)
        # Remove the beam as we pop back up the func call stack
        current_state_beam_array[row + 1][column] = "."

    # We reached a splitter, create two new traversals left first (DFS)
    if current_array_value == "|" and below_current_value == "^":
        current_state_beam_array[row + 1][column - 1] = "|"
        traverse_beam_array(current_state_beam_array, row + 1, column - 1)
        # Remove the previous path as we have already went that way
        current_state_beam_array[row + 1][column - 1] = "."

        current_state_beam_array[row + 1][column + 1] = "|"
        traverse_beam_array(current_state_beam_array, row + 1, column + 1)
        current_state_beam_array[row + 1][column + 1] = "."


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
        print("".join(line))


with FileInput("input.txt") as file_input:
    starting_manifold, starting_column = load_manifold(file_input)
    traverse_beam_array(starting_manifold, 0, starting_column)
    print(beam_count)
