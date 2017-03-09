"""
this module offers the functionality of serializing objects and restoring them
to memory.
"""

# python imports
import os
import pickle

# project imports
from dataHandlerAbstract import DataHandlerAbstract

class DataHandlerSerial(DataHandlerAbstract):
    def __init__(self, save_path = "XXX"):
        DataHandlerAbstract.__init__(self)
        if save_path == "XXX":
            path = os.path.dirname(os.path.realpath(__file__))
            add_path = "01_datasources/"
            save_path = os.path.join(path, add_path)
        self._save_path = save_path

    def get_all_employees(self):
        raise NotImplementedError

    def save_employees(self, employees):
        raise NotImplementedError

    def update_employee(self, employee):
        raise NotImplementedError

    def delete_employees(self, employees):
        raise NotImplementedError

a = DataHandlerSerial()