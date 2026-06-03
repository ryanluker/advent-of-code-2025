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


def construct_playground(file_input, iterations, debug_mode):
    # Setup a data structure of junction boxes with connected nodes
    circuits = []
    points = []
    for point in file_input:
        point_coord = [
            int(point)
            for point in point.strip().split(",")
        ]
        points.append(point_coord)
    
    point_distances = []
    for point in points:
        closest_point, distance = find_closest_point(point, points)
        circuits.append([{"coord": point, "connected_circuit": closest_point}])
        point_distances.append((point, closest_point, distance))

    # Sort the point distance pairings from shortest connection to longest
    # Note: we leverage the 3rd tuple value for the sort (distance)
    sorted_point_distances = sorted(point_distances, key=lambda x: x[2])
    # Split a sublist based on the number of iterations
    # Note: the points are sorted by the shortest connections to longest.
    for point, closest_point, _ in sorted_point_distances[:iterations]:
        circuit, _ = find_circuit_for_point(point, circuits)
        # "absorb" the existing closest circuit into the current one if not already.
        closest_circuit, _ = find_circuit_for_point(closest_point, circuits)
        if circuit != closest_circuit:
            circuit.extend(closest_circuit)
            circuits.remove(closest_circuit)

        if debug_mode:
            render_playground(circuits, debug_mode)

    return circuits


def find_circuit_for_point(point, circuits):
    for index, circuit in enumerate(circuits):
        for junc_box in circuit:
            if junc_box["coord"] == point:
                return circuit, junc_box
    # If we didn't find the point in the existing circuits, return None, None
    return None, None


def find_closest_point(origin, points):
    # Find the closest point based on straight line distance
    closest_point = None
    closest_distance = None
    for point in points:
        if origin == point:
            # Ignore the origin point's, point
            continue

        # Calculate the distance between the origin and the point
        origin_point_distance = calculate_straight_line_distance(origin, point)
        # Use the first point as the closest, as we have nothing to compare
        if closest_distance == None:
            closest_distance = origin_point_distance
            closest_point = point
            continue

        # If the distance is less than the current closest, swap
        if origin_point_distance < closest_distance:
            closest_point = point
            closest_distance = origin_point_distance

    return closest_point, closest_distance


def calculate_straight_line_distance(point_one, point_two):
    """
    Pass in two points (with 3 axis) and return the straight line distance
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
        for junc_box in circuit:
            # Each junc box has a coord attributs in x,y,z tuple
            xc = junc_box["coord"][0]
            yc = junc_box["coord"][1]
            zc = junc_box["coord"][2]
            ax.scatter(xc, yc, zc)

            # Add a line between the point and it's nearest neighbour
            if junc_box["connected_circuit"]:
                xcc = [xc, junc_box["connected_circuit"][0]]
                ycc = [yc, junc_box["connected_circuit"][1]]
                zcc = [zc, junc_box["connected_circuit"][2]]
                ax.plot(xcc, ycc, zcc, color='yellow', linewidth=2, marker='o')

    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    plt.show()


def run(file_name, run_mode, debug_mode):
    with FileInput(file_name) as file_input:
        # Set the number of "connections" based on the file_name
        if run_mode == "example":
            iterations = 10
        elif run_mode == "full":
            iterations = 1000
        else:
            raise Exception("File has no associated iteration amount")

        playground = construct_playground(file_input, iterations, debug_mode)
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

