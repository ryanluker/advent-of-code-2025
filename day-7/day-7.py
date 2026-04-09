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
    pass


def calculate_splits(beam_layout):
    pass


with FileInput("example_input.txt") as file_input:
    beam_layout = construct_beam_array(file_input)
    print(beam_layout)
    totals = calculate_splits(beam_layout)
    print(totals)
