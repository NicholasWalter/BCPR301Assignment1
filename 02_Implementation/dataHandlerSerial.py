"""
this module offers the functionality of serializing objects and restoring them
to memory.
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
        if save_path == "XXX":
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
                employees.append(pickle.load(open(f, "rb")))
            except:
                err_text = "Error reading file: {}"
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
        raise NotImplementedError

    def delete_employees(self, employees):
        raise NotImplementedError

a = DataHandlerSerial()