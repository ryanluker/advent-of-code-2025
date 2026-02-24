# Day 5 - Cafeteria
# IMS (Inventory Management System) is based on fresh ingredient ranges.
# EG 3-5 means IDs 3,4 and 5 are fresh, 2 would not be.
#
# Tactics:
# - Take the fresh ranges and apply them to a 1D array.
# - While constructing this array, deduplicate the ranges.
#
# Important Note:
# Lists cannot hold the full amount of fresh ids, instead we need
# to leverage python range functionality to reduce memory consumption.

from fileinput import FileInput


def remove_overlaps(database):
    items_modified = False
    # Remove and adjust any ranges with overlaps
    for index, fresh_range in enumerate(fresh_database):
        if index + 1 == len(fresh_database):
            # We are at the end and can quit
            continue

        next_fresh_range = fresh_database[index + 1]
        if fresh_range.stop >= next_fresh_range.start:
            # We have removed the current range in order to deduplicate the next
            fresh_database.pop(index)
            if fresh_range.stop <= next_fresh_range.stop:
                fresh_database[index] = range(fresh_range.start, next_fresh_range.stop)
            else:
                fresh_database[index] = range(fresh_range.start, fresh_range.stop)
            items_modified = True


    # Return if we modified anything during the overlap removal
    return items_modified


with FileInput("input.txt") as input:
    fresh_database = []
    # Construct the fresh ranges
    for fresh_range in input:
        if fresh_range == "\n":
            break
        fresh_range_params = fresh_range.strip("\n").split("-")
        fresh_row_range = range(
            int(fresh_range_params[0]), int(fresh_range_params[1])
        )
        # Kickoff the database if empty
        if len(fresh_database) == 0:
            fresh_database.append(fresh_row_range)
        
        # Look across the database for an ordered spot to put the range
        for index, item_range in enumerate(fresh_database):
            # Check if we can slot between the previous and current ranges cleanly
            if (
                item_range.start >= fresh_row_range.start and
                item_range.start >= fresh_row_range.stop
            ):
                fresh_database.insert(index, fresh_row_range)
                break
            
            # Check if we need to combine the current range with the new one
            if (
                item_range.start >= fresh_row_range.start and
                item_range.start <= fresh_row_range.stop
            ):
                combined_row_range = None
                if item_range.stop >= fresh_row_range.stop:
                    combined_row_range = range(fresh_row_range.start, item_range.stop)

                if item_range.stop <= fresh_row_range.stop:
                    combined_row_range = range(fresh_row_range.start, fresh_row_range.stop)

                fresh_database[index] = combined_row_range
                break
            
            # Check if the new range is already inside the existing one
            if (
                fresh_row_range.start >= item_range.start and
                fresh_row_range.stop <= item_range.stop
            ):
                # Do nothing as the range is already present in some form
                break

            # Check if we need to combine as the current range has a bigger stop
            # but also a bigger start (thus we need to use the new start)
            if (
                item_range.stop >= fresh_row_range.stop and
                item_range.start >= fresh_row_range.start
            ):
                combined_row_range = range(fresh_row_range.start, item_range.stop)
                fresh_database[index] = combined_row_range
                break

            # If we are at the end, we should append the range as the new fresh range is larger
            if index + 1 == len(fresh_database):
                fresh_database.append(fresh_row_range)

    # Remove and adjust any ranges with overlaps
    while True:
        items_removed = remove_overlaps(fresh_database)
        if not items_removed:
            # We have found all the overlaps
            break

    # Perform the final count
    fresh_count = 0
    for fresh_range in fresh_database:
        # Add one to the fresh_range length to account for range not being inclusive
        # EG: Range(1, 5) will only be 1,2,3,4 and not 5
        man_count = fresh_range.stop - fresh_range.start + 1
        print(f"deduped - {fresh_range} - {man_count}")
        fresh_count = fresh_count + man_count

    # Final fresh count
    print(f"Final fresh count: {fresh_count}")
