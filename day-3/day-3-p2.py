# Look at each joltage battery bank and find the 2 largest values, in order
# Tactics:
# Search over each bank and keep track of the highest numbers

from fileinput import FileInput

with FileInput("input.txt") as input:
    total_joltage_amount = 0
    for joltage_bank in input:
        joltage_bank = joltage_bank.strip("\n")
        if not joltage_bank:
            # We have hit the bottom of the joltage numbers
            continue

        # Turn the joltage from a single string of ints to list
        list_joltage_bank = list(joltage_bank)

        # Sort the joltage bank from highest to lowest
        sort_joltage_bank = sorted(list_joltage_bank, reverse=True)

        # Find the highest value that isn't in the last position
        max_joltage = None
        highest_value = sort_joltage_bank[0]
        highest_value_pos = list_joltage_bank.index(highest_value)
        if highest_value_pos == len(list_joltage_bank) - 1:
            # Highest value is in last position, used 2nd highest
            second_highest_value = sort_joltage_bank[1]
            second_highest_pos = list_joltage_bank.index(second_highest_value)
            max_joltage = str(second_highest_value) + str(highest_value)
            print(joltage_bank, max_joltage, highest_value_pos, second_highest_pos)
        else:
            # Highest value found, iterate until highest found in remainder
            # NOTE: exclude the current highest value from the remainder
            remaining_joltage_bank = list_joltage_bank[highest_value_pos + 1 :]
            sort_remaining = sorted(remaining_joltage_bank, reverse=True)
            # We simply want the highest remaining value as we care not about position
            highest_in_remaining = sort_remaining[0]
            max_joltage = str(highest_value) + str(highest_in_remaining)
            print(
                joltage_bank,
                max_joltage,
                highest_value_pos,
                remaining_joltage_bank.index(highest_in_remaining),
            )

        # Max joltage found for current bank
        total_joltage_amount = total_joltage_amount + int(max_joltage)

    # Final max joltage across all banks
    print(total_joltage_amount)
