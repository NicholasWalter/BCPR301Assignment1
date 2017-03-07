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
"""
this module offers the functionality of reading from and writing to the
save file
"""

# python imports
import util

# project imports
from dataHandlerAbstract import DataHandlerAbstract

class DataHandlerFile(DataHandlerAbstract):
    def __init__(self, file_path):
        Data
        self.file_path = file_path

    def save_employees(self, employees):
        raise NotImplementedError

    def save_employee(self, employee):
        raise NotImplementedError

    def get_all_employees(self):
        """
        reads the file this object was initiated with and returns all contained
        employees as Employee objects in a list
        """
        raise NotImplementedError
        with open(self.file) as source:
            for line in source:
                

    def get_employee(self, emp_id):
        raise NotImplementedError

    def employee_exists(self, employee):
        raise NotImplementedError

    def update_employee(self, employee):
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