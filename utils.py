# General Util functions for advent of code

import sys

def safe_argv_fetch(get_var, default):
    # Gather up the cli args
    # argv[0] - script name
    # argv[1] - puzzle day
    # argv[2] - run mode
    # argv[3] - debug mode
    try:
        if get_var == "puzzle_day":
            return sys.argv[1]
        elif get_var == "run_mode":
            return sys.argv[2]
        elif get_var == "debug_mode":
            if sys.argv[3] == "False":
                return False
            elif sys.argv[3] == "True":
                return True
            else:
                raise Exception("Incorrect debug mode, must be True or False")
    except IndexError:
        return default

