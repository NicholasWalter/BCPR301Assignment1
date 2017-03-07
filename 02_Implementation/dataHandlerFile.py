"""
reads data from and writes data to the configured csv file containing 
employee information
"""

# python imports
import datetime
import os

# project imports
import config
import employee
import inputConverter as IC
import util


def save_employees(to_save, target_file):
    """
    saves the supplied list of employees to the supplied save file
    """
    raise NotImplementedError

def get_all_employees(source_file = "XXX"):
    """
    reads all employees from the configured csv file
    @params: -
    @return:
        [[Employee],[String]] containing Employee objects and error string
    """
    if source_file == "XXX":
        source_file = util.get_config()["datasource"]

    result = []
    errors = []

    neccessary_keys = ["empid", "gender", "sales", "bmi", "salary", "birthday",
                        "age"]

    read_first_line = False
    with open(source_file) as file:
        line_counter = 1
        for line in file:
            if not read_first_line:             # ignore first line
                read_first_line = True
                continue
            try:
                split = line.split(",")         # split by comma
                attributes = {}

                # for each of the neccessary keys, get conversion, then add
                # to attributes
                for i in range(len(neccessary_keys)):
                    key = neccessary_keys[i]
                    attributes[key] = IC.convert_input(split[i], key)

                attributes["age"] = utils.calculate_age(attributes["birthday"])
                new_age = util.calculate_age(new_birthday)
                results.append(employee.create_employee())
            except ValueError as verr:
                errors.append("Error on line {}: ".format(line_counter)+
                                str(verr))
            line_counter += 1
    return[result, errors]

def check_if_employee_exists(to_check):
    """
    checks if the supplied employee already exists in the csv file
    @params:
        to_check: employee to check
    @return:
        true if the employee exists, otherwise false
    """
    raise NotImplementedError

################################################################################
## Testing functionality                                                      ##
################################################################################

def test_get_all_employees():
    this = os.path.dirname(os.path.realpath(__file__))
    file = "01_datasources/employees.csv"
    read_employees = get_all_employees(os.path.join(this, file))
    for emp in read_employees:
        print(emp)

if __name__ == "__main__":
    test_get_all_employees()
