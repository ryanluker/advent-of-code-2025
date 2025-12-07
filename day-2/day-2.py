# Open the csv file and iterate across the entries
# Search for invalid IDs across product id ranges
# Invalid IDS consist of the following:
#   - IDs with twice repeated digit sequences
#   - IDs with leading zeros (none exist)
# Add up all invalid ids and print total

import csv


def is_invalid_check(id):
    return True


with open("example-input.csv") as csv_file:
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
