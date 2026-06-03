# Day 8 - Playground Part 2
# https://adventofcode.com/2025/day/8
# https://en.wikipedia.org/wiki/Euclidean_distance
# 
# Tactics:
# - Construct a temp data structure with each junction box and it's nearest neighbour
# - Order the list based on the distance between the boxes
# - Peel off the boxes as they are connected
# - Keep track of the connected circuits as they grow
# 
# Research:
# - Octree for the 3d points (https://en.wikipedia.org/wiki/Octree)
# 

from fileinput import FileInput
import matplotlib.pyplot as plt
import math


def run(file_name, run_mode, debug_mode):
    with FileInput(file_name) as file_input:
        # Set the number of "connections" based on the file_name
        if run_mode == "example":
            iterations = 10
        elif run_mode == "full":
            iterations = 1000
        else:
            raise Exception("File has no associated iteration amount")
