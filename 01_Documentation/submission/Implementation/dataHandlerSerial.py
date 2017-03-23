"""
this module offers the functionality of serializing objects and restoring them
to memory. All objects will be stored in files with their employee id as name
and .emp as extension.

this module cannot be tested using doctest or unit test because results change
with the state of the data source
"""

# python imports
from glob import glob
import os
import pickle

# project imports
from dataHandlerAbstract import DataHandlerAbstract
import IOHelper as IO


class DataHandlerSerial(DataHandlerAbstract):
    def __init__(self, save_path = "XXX"):
        DataHandlerAbstract.__init__(self)
        if save_path == "XXX":              # default path is "01_datasources/"
            path = os.path.dirname(os.path.realpath(__file__))
            add_path = "01_datasources/"
            save_path = os.path.join(path, add_path)
        self._save_path = save_path

    def get_all_employees(self):
        os.chdir(self._save_path)
        all_files = glob("*.emp")
        employees = []

        for f in all_files:
            try:
                new_emp = pickle.load(open(f, "rb"))
                if type(new_emp).__name__ == "Employee":
                    employees.append(new_emp)
                else:
                    err_text = "File {} does not contain an employee object."
                    IO.stdErr(err_text.format(f))
            except:
                err_text = "Could not read file: {}"
                IO.stdErr(err_text.format(f))
        return employees

    def save_employees(self, employees):
        for emp in employees:
            try:
                file_name = "{}.emp".format(emp.employee_id)
                file_path = os.path.join(self._save_path, file_name)
                pickle.dump(emp, open(file_path, "wb"))
            except:
                err_text = "Could not serialise {}"
                IO.stdErr(err_text.format(emp.employee_id))

    def update_employee(self, employee):
        os.chdir(self._save_path)
        target_file = "{}.emp".format(employee.employee_id)
        if not os.path.isfile(target_file):
            IO.stdErr("Could not find the supplied employee to update")
            return
        self.save_employees([employee])

    def delete_employees(self, employee_ids):
        os.chdir(self._save_path)
        for id in employee_ids:
            try:
                os.remove("{}.emp".format(id))
            except:
                IO.stdErr("Could not delete employee {}".format(id))

a = DataHandlerSerial()