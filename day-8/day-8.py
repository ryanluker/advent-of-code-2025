# Day 8 - Playground
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


def construct_playground(file_input, debug_mode):
    # Take the input file and load each coordinate set
    # (OPT) Cluster the coordinates based on their distance from each other
    # Iterate over the coords
    circuits = []
    for junction in file_input:
        circuit = []
        junc_coord = junction.strip().split(',')
        junc_box = {
            "coord": (int(junc_coord[0]), int(junc_coord[1]), int(junc_coord[2])),
            "connected_circuit": None,
        }
        # Add the junction box to the circuit
        circuit.append(junc_box)
        # Add the circuit to the overall list if not yet done
        circuits.append(circuit)
    return circuits


def print_playground(playground, debug_mode):
    # Take the finished playground and print the 3 largest circuits
    # Sort the playground circuits from smallest to largest
    playground.sort(key=len)
    first_circuit = playground[-1]
    second_circuit = playground[-2]
    third_circuit = playground[-3]
    print(f"""3 Largest circuits:
        {first_circuit}
        ---------------
        {second_circuit}
        ---------------
        {third_circuit}
        ---------------
    """)
    print(f"Multiplied total: {len(first_circuit), len(second_circuit), len(third_circuit)} = {len(first_circuit) * len(second_circuit) * len(third_circuit)}")


def run(file_name, debug_mode):
    with FileInput(file_name) as file_input:
        playground = construct_playground(file_input, debug_mode)
        print_playground(playground, debug_mode)
