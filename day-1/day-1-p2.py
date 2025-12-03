from fileinput import FileInput

# Create a list from 0 <-> 99 positions
lock_dial = [{"visits": 0, "dial": dial} for dial in range(0, 100)]

# Read in the input.txt file and use the directions to move between the 0..99 spots
dial_movements: list[str] = []
with FileInput("input.txt") as input:
    for line in input:
        movement = line.strip("\n")
        dial_movements.append(movement)

# The starting point is dial position 50
current_dial_position = 50

# The list positions 0 and 99 "flip" over depending on your direction of travel
for perform_movement in dial_movements:
    if perform_movement == "":
        break

    # Get the direction of travel
    direction = perform_movement[0]
    # Get the number of movements
    movements = int(perform_movement[1:])

    # Peform the number of movements directed by the inputs
    for _ in range(0, movements):
        if direction == "R":
            # Spin the dial in the "clockwise" direction (aka positive)
            future_dial_position = current_dial_position + 1
            if future_dial_position == 100:
                current_dial_position = 0
            else:
                current_dial_position += 1
        elif direction == "L":
            # Sprint the dial in the "counter-clockwise" direction (aka negative)
            future_dial_position = current_dial_position - 1
            if future_dial_position == -1:
                current_dial_position = 99
            else:
                current_dial_position -= 1
        else:
            raise AttributeError(f"Unknown direction? {direction, movements}")

        # Add a visit to the current dial position
        lock_dial[current_dial_position]["visits"] += 1

# Print the state of the lock_dial
print(lock_dial[0])
