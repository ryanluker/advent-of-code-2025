# Day 5 - Cafeteria
# IMS is based on fresh ingredient ranges.
# EG 3-5 means IDs 3,4 and 5 are fresh, 2 would not be.
#
# Tactics:
# - Take the fresh ranges and apply them to a 1D array.
# - While constructing this array, deduplicate the ranges.
# - EG 2-4 would already be partially covered by 3 and 4 above.
# - When finding out if an ID is "fresh" simply look up the value.
#
# Important Note:
# Lists cannot hold the full amount of fresh ids, instead we need
# to leverage python range functionality to reduce memory consumption.

from fileinput import FileInput


with FileInput("input.txt") as input:
    fresh_database = []
    # Construct the fresh ranges
    for fresh_range in input:
        if fresh_range == "\n":
            break
        fresh_range_params = fresh_range.strip("\n").split("-")
        fresh_row_range = range(
            int(fresh_range_params[0]), int(fresh_range_params[1]) + 1
        )
        # Store the python ranges in a list
        fresh_database.append(fresh_row_range)

    fresh_count = 0
    # Look through the food ids for fresh items
    for fresh_item in input:
        if fresh_item == "":
            break
        fresh_id_item = int(fresh_item.strip("\n"))
        # Find if the fresh_id we are looking up, exists in the database
        # Note: Leverage range to find out if an item in within
        for fresh_range in fresh_database:
            try:
                fresh_range.index(fresh_id_item)
                fresh_count = fresh_count + 1
                # Once we know the fresh item was in one range, skip the rest
                break
            except:
                # Fresh Item isn't within the current range
                continue


    # Final fresh count
    print(f"Final fresh count: {fresh_count}")
