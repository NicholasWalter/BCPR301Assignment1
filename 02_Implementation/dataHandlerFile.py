"""
reads data from and writes data to the configured csv file containing 
employee information
"""

# python imports
import datetime

# project imports
import config
import employee
import util


def save_employees(to_save, target_file):
    """
    saves the supplied list of employees to the supplied save file
    """

def get_all_employees():
    """
    reads all employees from the configured csv file
    @params: -
    @return:
        [[Employee],[String]] containing Employee objects and error string
    """
    result = []
    errors = []

    source_file = config.get_config()["datasource"]
    read_first_line = False
    with open(source_file) as file:
        for line in file:
            if not read_first_line:
                read_first_line = True
                continue
            split = line.split(",")
            try:
                

