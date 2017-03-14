"""
this module serves as entry point to the program.
depending on the command line arguments supplied it will start either the
gui or the cmd version of the program
"""

# python imports
import sys

# project imports
import administratorCMD as CMD
import IOHelper as IO

def start():
    IO.initialize(CMD)
    line = ""
    if not len(sys.argv) == 1:
        for i in range(1, len(sys.argv)):
            line += sys.argv[i] + " "
    CMD.start(sys.argv[1:])

if __name__ == "__main__":
    start()