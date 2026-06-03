# Generic runner for the advent of code 2025 puzzles

from importlib import import_module
from utils import safe_argv_fetch


def main():
    day = safe_argv_fetch("puzzle_day", None)
    if day == None:
        raise Exception("Puzzle day is required!")
    
    # All day modules have two txt files, one example and the full
    run_mode = safe_argv_fetch("run_mode", "example-input.txt")
    if run_mode == "example":
        input_filepath = f"{day}/example-input.txt"
    elif run_mode == "full":
        input_filepath = f"{day}/input.txt"
    else:
        raise Exception("Incorrect run_mode!")

    # Part 1 or Part 2
    part = safe_argv_fetch("part_mode", "part1")

    debug_mode = safe_argv_fetch("debug_mode", False)

    day_module = import_module(f"{day}.{day}-{part}").run(input_filepath, run_mode, debug_mode)
    # Most day modules auto run and do not require func calling


if __name__ == "__main__":
    main()

