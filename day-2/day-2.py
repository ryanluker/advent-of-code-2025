# Open the csv file and iterate across the entries
# Search for invalid IDs across product id ranges
# Invalid IDS consist of the following:
#   - IDs with twice repeated digit sequences
#   - IDs with leading zeros (none exist)
# Add up all invalid ids and print total

import csv


def is_invalid_check(id):
    """Checks for invalid repeating product ids"""
    str_id = str(id)
    id_len = len(str_id)

    # Calculate the middle index differently for 2 len
    if id_len == 2:
        # Example 1|1 -> first:1, back:1
        # Grab the first half of the product number
        first_half = str_id[0]
        # Grab the back half of the product number
        back_half = str_id[1]
    elif id_len % 2:
        # Ignore un-even product ids as they can never repeat
        return False
    else:
        # Find the middle index and offset by 1
        # Example 11885|11885 -> int(10/2) == 4
        middle_index = int(id_len / 2)
        # Grab the first half of the product number
        first_half = str_id[:middle_index]
        # Grab the back half of the product number
        back_half = str_id[middle_index:]

    # Example 3859|3859 -> first:3859, back:3859
    if first_half == back_half:
        return True
    else:
        return False


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
