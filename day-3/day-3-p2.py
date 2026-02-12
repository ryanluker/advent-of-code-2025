# Look at each joltage battery bank and find the 12 largest values, in order

from fileinput import FileInput


with FileInput("input.txt") as input:
    total_joltage_amount = 0
    for joltage_bank in input:
        joltage_bank = joltage_bank.strip("\n")
        if not joltage_bank:
            # We have hit the bottom of the joltage numbers
            continue
        
        fab_joltage_bank = []
        list_joltage_bank = list(joltage_bank)
        # Find the biggest jolt to start at
        # Note: avoid picking a big number near the end of the bank
        highest_jolt = 0
        highest_jolt_index = None
        for index, jolt in enumerate(list_joltage_bank):
            # Once we get near the end, avoid picking high jolts
            if index >= len(list_joltage_bank) - 11:
                break
            if highest_jolt < int(jolt):
                highest_jolt = int(jolt)
                highest_jolt_index = index
        
        # Store the highest jolt and continue
        fab_joltage_bank.append(highest_jolt)

        # Grab the remainder of the bank for processing
        subset_joltage_bank = list_joltage_bank[highest_jolt_index + 1:]
        for jolt in subset_joltage_bank:
            # Fill up the fab with jolts to start
            if len(fab_joltage_bank) <= 11:
                fab_joltage_bank.append(int(jolt))
                print(fab_joltage_bank)
                continue
            # Once full, start to pop small numbers from the front and add numbers to the rear
            for fab_index, fab_jolt in enumerate(fab_joltage_bank):
                # Account for the last spot in the fab jolk bank
                if fab_index == len(fab_joltage_bank) - 1:
                    # If the last jolt is larger than the last fab jolt, swap
                    if fab_jolt < int(jolt):
                        fab_joltage_bank.pop(fab_index)
                        fab_joltage_bank.append(int(jolt))
                    break
                # Check if the next jolt should be used instead
                if fab_jolt < fab_joltage_bank[fab_index + 1]:
                    fab_joltage_bank.pop(fab_index)
                    fab_joltage_bank.append(int(jolt))
                    print(fab_joltage_bank)
                    break
            print(fab_joltage_bank)
        
        print(f"Finished generating joltage {joltage_bank} - {fab_joltage_bank}")
        # Concat finished fab bank into a single string and add it to the total
        int_fab_joltage_bank = int("".join([str(fab_joltage) for fab_joltage in fab_joltage_bank]))
        print(f"Final bank: {int_fab_joltage_bank}")
        total_joltage_amount = total_joltage_amount + int_fab_joltage_bank
        print(f"Total joltage amount {total_joltage_amount}")
