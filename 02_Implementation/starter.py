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
    CMD.start()

if __name__ == "__main__":
    start()