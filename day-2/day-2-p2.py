# Open the csv file and iterate across the entries
# Search for invalid IDs across product id ranges
# Invalid IDS consist of the following:
#   - IDs with twice repeated digit sequences
#   - IDs with leading zeros (none exist)
# Add up all invalid ids and print total

import csv


def is_invalid_check(id):
    """Checks for invalid repeating product ids"""
    # Extract a character at a time and check for repeats
    str_id = str(id)
    for index in range(len(str_id)):
        # Check if str_id segment is repeating
        str_id_segment = str_id[index + 1 :]
        found_segments = str_id.count(str_id_segment)

        # If the found segments match the length of str_id we have repeating
        # digits like: 11111, 222, 11, etc
        if found_segments == len(str_id):
            return True

        # If the number of found segments * the length of segment matches
        # matches the length of str_id we have a repeating pattern.
        # EG: 121121121 -> found_segments=3, str_id_segment=3, len(str_id)=9
        if found_segments * len(str_id_segment) == len(str_id):
            return True


with open("input.csv") as csv_file:
    # Open the csv file with the builtin lang reader
    input_reader = csv.reader(csv_file, delimiter=",")

    # Find all possible ids within the ranges
    id_ranges = [row for row in input_reader][0]
    possible_ids = []
    for id_range in id_ranges:
        # create a range by striping the dash
        # EG: 11-22 will become (11, 22)
        start_range, end_range = tuple(int(entry) for entry in id_range.split("-"))
        [possible_ids.append(id) for id in range(start_range, end_range + 1)]

    # Take the possible ids and find the invalids
    invalid_ids = [id for id in possible_ids if is_invalid_check(id)]

    # Sum the invalids and print
    invalid_sum = 0
    for invalid_id in invalid_ids:
        invalid_sum += invalid_id

    print(f"Invalid IDs: {invalid_ids}")
    print(f"Invalid Sum: {invalid_sum}")
