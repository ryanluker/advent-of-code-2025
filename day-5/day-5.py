# Day 5 - Cafeteria
# IMS is based on fresh ingredient ranges.
# EG 3-5 means IDs 3,4 and 5 are fresh, 2 would not be.
#
# Tactics:
# - Take the fresh ranges and apply them to a 1D array.
# - While constructing this array, deduplicate the ranges.
# - EG 2-4 would already be partially covered by 3 and 4 above.
# - When finding out if an ID is "fresh" simply look up the value.

from fileinput import FileInput

with FileInput("example-input.txt") as input:
    fresh_database = []
    # Construct the fresh ranges
    for fresh_range in input:
        if fresh_range == "\n":
            break
        fresh_range_params = fresh_range.strip("\n").split("-")
        fresh_row_range = list(
            range(
                int(fresh_range_params[0]), int(fresh_range_params[1])
            )
        )

        # Loop over the fresh database and find a spot for the new ids

    print(fresh_database)

    # Look through the food ids for fresh items
    for fresh_item in input:
        print(fresh_item)
        if fresh_item == "":
            break
