"""
this module offers the DataHandlerDataBase class, opening connections to a
MySQL database to save and read employees to and from.
"""

# python imports
import pymysql

# project imports
from dataHandlerAbstract import DataHandlerAbstract

class DataHandlerDatabase(DataHandlerAbstract):
    
    def __init__(self, db_ip, db_username, db_password, db):
        self.db_ip = db_ip
        self.db_username = db_username
        self.db_password = db_password
        self.db = db

    def _execute_command(self, command):
        db = pymysql.connect(self.db_ip, self.db_username, self.db_password,
                                self.db)
        output = []
        cursor = db.cursor()
        cursor.execute(command)

        line = cursor.fetchone()
        while line is not None:
            output.append(line)
            line = cursor.fetchone()

        db.close()
        return output

    def get_all_employees(self):
        command = "SELECT * FROM employees"
        lines = self._execute_command(command)
        # TODO

    def save_employees(employees):
        c = 'INSERT INTO employees VALUES' + \
            '({}", "{}", "{}", "{}", "{}", "{}", "{}")'
        for emp in employees:
            command = c.format(e.employee_id, e.gender, e.age, e.sales, e.bmi,
                                e.salary, e.get_birthday_string())
            result = self._execute_command(command)
            if result[0].startswith("Query OK"):
                continue
            # TODO: Error handling, should usually not occure because of data
            # validation


################################################################################
## Testing functionality                                                      ##
################################################################################

def _get_test_object():
    return DataHandlerDatabase("localhost", "pyaccess", "bcpr301",
                                "bcpr301_assignment1")

def _test_get_all_employees():
    db = _get_test_object()
    db.get_all_employees()

def _do_all_tests():
    _test_get_all_employees()

if __name__ == "__main__":
    _do_all_tests()