"""
reads data from and writes data to the configured csv file containing 
employee information
"""

import config
import employee


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
                emp_id = split[0]                           # stays string
                gender = split[1]                           # stays string
                sales = int(split[2])                       # integer
                bmi = split[3]                              # stays string
                salary = int(split[4])                      # integer
                birthday_split = split[5].split("-")        # birthday in three parts
                year = int(birthday_split[0])               # integer
                month = int(birthday_split[1])              # integer
                day = int(birthday_split[2])                # integer
                bd = datetime.datetime(year, month, day)
                new_employee = employee.Employee(split[0], split[1], split[2], split[3])

