"""
this module serves as entry point to the program.
depending on the command line arguments supplied it will start either the
gui or the cmd version of the program

there is nothing to test here.
"""

# python imports
import sys

# project imports
import administratorCMD as CMD
import IOHelper as IO


def start():
    instance = CMD.AdministratorCMD()
    IO.initialize(instance)
    CMD.start(sys.argv[1:], instance)

if __name__ == "__main__":
    start()
