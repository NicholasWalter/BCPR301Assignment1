"""
this module serves as entry point to the program.
depending on the command line arguments supplied it will start either the
gui or the cmd version of the program
"""

# python imports
import sys

# project imports
import administratorGUI as GUI
import administratorCMD as CMD
import IOHelper as IO

def start():
    if len(sys.argv) != 2:
        print_usage()
        sys.exit()
    try:
        startup_types[sys.argv[1]]()
    except KeyError:
        print_usage()
        sys.exit()

def start_cmd():
    IO.initialize(CMD)
    CMD.start()

def start_gui():
    IO.initialize(GUI)
    GUI.start()

def print_usage():
    print("Usage:")
    print("python3.x starter.py [arg]")
    print("\nArguments:")
    print(" cmd: starts the program in the command line")
    print(" gui: starts the program with a GUI")
    print(" help: shows this help screen")

startup_types = {"cmd": start_cmd, "gui": start_gui, "help": print_usage}

if __name__ == "__main__":
    start()