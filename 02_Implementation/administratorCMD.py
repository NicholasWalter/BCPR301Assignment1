"""
this module offers a command line interface to the functionality of the program.
"""

# python imports
import sys

# project imports
import dataHandlerFacade as dataHandler
import util

def start():
    print("starting CMD")
    while True:
        command = input("User command: ")
        try:
            commands[command](command)
        except KeyError:
            print_error_help()

def print_error_help(command):
    print("This is not a valid command. Use \"help\" to get a list of commands")

def print_help(command):
    print("Available commands:")
    print("list employees:\n    lists all saved employees")
    print("synchronize:\n    synchronize all datasources")
    print("help:\n    displays this help menu")
    print("exit:\n    terminates the program")

def display_statistic(command):
    parts = command.split(" ")
    statistic = parts[1]
    group = parts[2]
    print("displaying all {} grouped by {}".format(statistic, group))
    # TODO
    raise NotImplementedError

def display_all_employees(command):
    all_employees = dataHandler.get_all_employees()
    for emp in all_employees:
        print(emp)

def stdOut(message):
    print(message)

def stdErr(message):
    print("Error: " + message)

commands = {"help": print_help, "list employees": display_all_employees,
            "synchronize": dataHandler.sync_datasources, "exit": util.exit}