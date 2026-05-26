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
import matplotlib.pyplot as plt
import math


def construct_playground(file_input, debug_mode):
    # Setup a data structure of junction boxes with connected nodes
    points = []
    for point in file_input:
        point_coord = [
            int(point)
            for point in point.strip().split(",")
        ]
        points.append(point_coord)

    circuits = []
    for point in points:
        junc_box = {"coord": point}
        closest_point = find_closest_point(point, points)
        junc_box["connected_circuit"] = closest_point
        circuits.append(junc_box)

        if debug_mode:
            render_playground(circuits, debug_mode)

    return circuits


def find_closest_point(origin, points):
    # Find the closest point based on straight line distance
    closest_point = None
    for point in points:
        if origin == point:
            # Ignore the origin points, point
            continue
        
        if closest_point == None:
            closest_point = point
            continue

        # Calculate the distance between the origin and the point
        origin_point_distance = calculate_straight_line_distance(origin, point)
        # If the distance is less than the current closest, swap
        origin_closest_distance = calculate_straight_line_distance(origin, closest_point)
        if origin_point_distance < origin_closest_distance:
            closest_point = point

    return closest_point


def calculate_straight_line_distance(point_one, point_two):
    """
    Pass in two points (with 3 axis) and return the distance
    """
    x_calc = (point_one[0] - point_two[0]) ** 2
    y_calc = (point_one[1] - point_two[1]) ** 2
    z_calc = (point_one[2] - point_two[2]) ** 2
    return math.sqrt(x_calc + y_calc + z_calc)


def render_playground(playground, debug_mode):
    # Print the 3d plot of the playground
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    
    for circuit in playground:
        # Each circuit has a coord attributs in x,y,z tuple
        xc = circuit["coord"][0]
        yc = circuit["coord"][1]
        zc = circuit["coord"][2]
        ax.scatter(xc, yc, zc)

        # Add a line between the point and it's nearest neighbour
        if circuit["connected_circuit"]:
            xcc = [xc, circuit["connected_circuit"][0]]
            ycc = [yc, circuit["connected_circuit"][1]]
            zcc = [zc, circuit["connected_circuit"][2]]
            ax.plot(xcc, ycc, zcc, color='yellow', linewidth=2, marker='o')

    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    plt.show()


def run(file_name, debug_mode):
    with FileInput(file_name) as file_input:
        playground = construct_playground(file_input, debug_mode)
        # Visualize the final playground before printing the 3 largest circuits
        render_playground(playground, debug_mode)

        # Take the finished playground and print the 3 largest circuits
        # Sort the playground circuits from smallest to largest
        playground.sort(key=len)
        first_circuit = playground[-1]
        second_circuit = playground[-2]
        third_circuit = playground[-3]
        print(f"""
            3 Largest circuits:
            {first_circuit}
            ---------------
            {second_circuit}
            ---------------
            {third_circuit}
            ---------------
        """)
        print(f"Multiplied total: {len(first_circuit), len(second_circuit), len(third_circuit)} = {len(first_circuit) * len(second_circuit) * len(third_circuit)}")

