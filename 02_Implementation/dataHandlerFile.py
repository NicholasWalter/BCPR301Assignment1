"""
reads data from and writes data to the configured csv file containing 
employee information
"""

# python imports
import abc
import datetime
import os

# project imports
import config
from dataHandlerAbstract import DataHandlerAbstract
import employee
import inputConverter as IC


class DataHandlerFile(DataHandlerAbstract):
    def __init__(self, file_path):
        """
        initiates a DataHandlerFile object with the supplied file as datasource.
        """
        DataHandlerAbstract.__init__(self)
        self._file = file_path

    def get_all_employees(self):
        """
        reads the file this object was initiated with and returns all contained
        employees as Employee objects in a list
        @params: -
        @return: list of Employee objects, may be empty
        """
        employees = []

        # using file as a resource so I dont forget to close it
        with open(self._file) as source:
            skipped_first = False
            for line in source:
                if not skipped_first:
                    skipped_first = True
                    continue
                split = line.split(",")
                # TODO: HIGH: validate data
                emp_id = split[0]
                gender = split[1]
                sales = int(split[2])
                bmi = split[3]
                salary = int(split[4])
                split2 = split[5].split("-")
                year = int(split2[0])
                month = int(split2[1])
                day = int(split2[2])
                bday = datetime.date(year, month, day)
                age = int(split[6])
                attributes = {"empid": emp_id, "gender": gender, "sales": sales,
                                "bmi": bmi, "salary": salary, "birthday": bday,
                                "age": age}
                # TODO: high: catch ValueError from employee creation
                employees.append(employee.create_employee(attributes))
        return employees

    def save_employees(self, employees):
        """
        saves the provided list of employees to the datasource
        NOTE: use employee_exists() before using this to make sure no duplicates
        are created!
        @params:
            employees: List of Employee objects to save
        @return: -
        """
        # TODO: HIGH: check if employees exist first, ignore description
        new_lines = [emp.get_csv_line() for emp in employees]
        with open(self._file, "a") as target:
            for line in new_lines:
                target.write(line)

    def update_employee(self, employee):
        """
        updates the record for the supplied Employee object
        if no employee record with the supplied employee id exists,
        nothing happens. use save_employee for this.
        @params:
            employee: The Employee object for which to update the record
        @return: -
        """
        lines = []
        with open(self._file) as source:
            for line in source:
                split = line.split(",")
                if split[0] == employee.employee_id:
                    lines.append(employee.get_csv_line())
                    continue
                lines.append(line)

        with open(self._file, "w") as target:
            for line in lines:
                target.write(line)

    def delete_employees(self, employees):
        ids = [emp.employee_id for emp in employees]
        lines = []
        with open(self._file) as source:
            for line in source:
                split = line.split(",")
                if split[0] in ids:
                    continue
                line.append(line)

        with open(self._file, "w") as target:
            for line in lines:
                target.write(line)

################################################################################
## Testing functionality                                                      ##
################################################################################

def _get_test_object():
    path = os.path.dirname(os.path.realpath(__file__))
    file = "01_datasources/employees.csv"
    full_path = os.path.join(path, file)
    return DataHandlerFile(full_path)

def _test_get_all_employees():
    data = _get_test_object()
    [print(emp) for emp in data.get_all_employees()]

def _test_employee_exists():
    data = _get_test_object()
    print("should be True: {}".format(data.employee_exists("A123")))
    print("should be False: {}".format(data.employee_exists("X789")))

def _test_update_employee():
    bday = datetime.date(1995, 10, 14)
    new_emp = employee.Employee("A123", "m", 999, "normal", 77, bday, 21)
    new_emp2 = employee.Employee("X999", "m", 2, "normal", 77, bday, 21)
    data = _get_test_object()
    data.update_employee(new_emp)
    data.update_employee(new_emp2)

def _test_get_employee():
    bday = datetime.date(1995, 10, 14)
    test_emp = employee.Employee("A123", "m", 2, "normal", 77, bday, 21)
    data = _get_test_object()
    got_emp = data.get_employee("A123")
    print("should be True: {}".format(test_emp.equals(got_emp)))

def _test_save_employee():
    bday = datetime.date(1995, 10, 14)
    test_emp = employee.Employee("A234", "m", 2, "normal", 77, bday, 21)
    data = _get_test_object()
    data.save_employee(test_emp)

if __name__ == "__main__":
    _test_get_all_employees()
    _test_employee_exists()
    _test_update_employee()
    _test_get_employee()
    _test_save_employee()