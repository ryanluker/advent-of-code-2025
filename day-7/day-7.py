# Day 7: Laboratories
# Beam printer
#
# Tactics:
#
#
# Example:
# ....S....
# ....|....
# ...|^|...
# ...|.|...
# ..|^|^|..


from fileinput import FileInput


def construct_beam_array(file_input):
    beam_layout = []
    totals = 0
    for row, line in enumerate(file_input):
        striped_line = line.strip()
        beam_layout.append([])
        for column, char in enumerate(striped_line):
            # We jump out the top early if we are on the first row.
            if row == 0:
                beam_layout[row].append(char)
                continue

            # By default, append the character to the beam layout.
            beam_layout[row].append(char)
            
            # Store the value above the current box for later reference.
            above_box_value = beam_layout[row - 1][column]
            
            # Check for the beam splitter character "^" and add a beam to each side
            current_box_value = beam_layout[row][column]
            if current_box_value == "^" and above_box_value == "|":
                beam_layout[row][column - 1] = "|"
                # Keep track of the beam splitting
                totals = totals + 1
                continue

            # If the previous box is a beam splitter, we need to adjust the current box value.
            neg_one_above_box_value = beam_layout[row - 1][column - 1]
            if beam_layout[row][column - 1] == "^" and neg_one_above_box_value:
                beam_layout[row][column] = "|"
                continue

            
            # Check the above character is a line and if so, add a beam.
            if above_box_value == "|" and current_box_value == ".":
                beam_layout[row][column] = "|"
                continue

            # Check for the starting charcater "S" above the current spot.
            elif above_box_value == "S" and current_box_value == ".":
                beam_layout[row][column] = "|"
                continue

    return beam_layout, totals


def print_layout(beam_layout):
    """Pretty prints the beam layout for human visualization."""
    for line in beam_layout:
        print("".join(line))


with FileInput("input.txt") as file_input:
    beam_layout, totals = construct_beam_array(file_input)
    print_layout(beam_layout)
    print(totals)
