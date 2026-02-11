# Look at each joltage battery bank and find the 12 largest values, in order
# Tactics:
#   - Look for the biggest value that is not near the end (must be min, 12 away)
#   - Always prefer the bigger numbers near the front
#   - After finding the first number, create a subset to find the remaining values
#   - Might be a good scenario for a recursive design

from fileinput import FileInput


def find_the_next_highest_value(current_subset):
    current_highest = 0
    for item in current_subset:
        int_item = int(item)
        if current_highest < int_item:
            # New highest item
            current_highest = int_item
        # Current highest still biggest
    return current_highest

with FileInput("example-input.txt") as input:
    total_joltage_amount = 0
    for joltage_bank in input:
        joltage_bank = joltage_bank.strip("\n")
        if not joltage_bank:
            # We have hit the bottom of the joltage numbers
            continue
        # Creates a pre-allocated list 12 items long
        pre_fab_joltage_bank = [None] * 12
        current_joltage_bank = list(joltage_bank)
        for turn in range(0, len(pre_fab_joltage_bank)):
            # Find the highest outstanding value
            high_value = find_the_next_highest_value(current_joltage_bank)
            try:
                index_high = current_joltage_bank.index(str(high_value))
            except:
                print(f"------High value too close to end------")
            pre_fab_joltage_bank[turn] = high_value
            current_joltage_bank = current_joltage_bank[index_high+1:]
        print(f"Finished generating joltage {joltage_bank} - {pre_fab_joltage_bank}")
