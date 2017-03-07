"""
reads data from and writes data to the configured csv file containing 
employee information
"""

# python imports
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

    def save_employees(self, employees):
        """
        saves the provided list of employees to the datasource
        NOTE: use employee_exists() before using this to make sure no duplicates
        are created!
        @params:
            employees: List of Employee objects to save
        @return: -
        """
        new_lines = [emp.get_csv_line() for emp in employees]
        with open(self._file, "a") as target:
            for line in new_lines:
                target.write(line)

        raise NotImplementedError

    def save_employee(self, employee):
        """
        saves the provided employee to the data source
        @params:
            employee: Employee object to save
        @return: -
        """
        self.save_employees([employee])[0]

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
                attributes = {"empid": empid, "gender": gender, "sales": sales,
                                "bmi": bmi, "salary": salary, "birthday": bday,
                                "age": age}
                # TODO: high: catch ValueError from employee creation
                employees.append(employee.create_employee(attributes))
        return employees


    def get_employee(self, emp_id):
        """
        gets the Employee object for the employee with the specified id.
        if the employee id does not exist in the data source, will return None
        @params:
            emp_id: String: employee id to look for
        @return:
            Employee object if an employee with the id exists, otherwise None
            Since the employee id should be unique, returns the first employee
            encountered in traversing the list that fits
        """
        all_employees = self.get_all_employees()
        for emp in all_employees:
            if emp.employee_id == emp_id:
                return emp
        return None
        
    def employee_exists(self, emp_id):
        """
        checks if an employee with the provided id exists in the datasource
        @params:
            emp_id: String: employee id to check
        @return:
            True if the employee exists, otherwise False
        """
        return not self.get_employee(emp_id) is None

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

################################################################################
## Testing functionality                                                      ##
################################################################################



if __name__ == "__main__":
    pass