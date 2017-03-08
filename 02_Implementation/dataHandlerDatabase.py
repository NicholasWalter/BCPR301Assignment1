"""
this module offers the DataHandlerDataBase class, opening connections to a
MySQL database to save and read employees to and from.

This does NOT protect against SQL injection at all
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

    def get_all_employees(self):
        raise NotImplementedError
        command = "SELECT * FROM employees"
        lines = self._execute_command(command)
        # TODO: parse lines, return employees
    
    def save_employees(self, employees):
        raise NotImplementedError
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

    def update_employee(self, emp):
        raise NotImplementedError
        c = "UPDATE employees SET gender = "{}", age = {}, sales = {}, " + \
            'bmi = "{}", salary = {}, birthday = "{}" WHERE id = "{}"'
        command = c.format(emp.gender, emp.age, emp.sales, emp.bmi, emp.salary,
                            emp.birthday, emp.employee_id)
        result = self._execute_command(command)
        if result[0].startswith("Query OK"):
            continue
        # TODO: Error handling
        

    def delete_employees(self, employees):
        raise NotImplementedError
        c = 'DELETE FROM employees WHERE id = {}'
        for emp in employees:
            command = c.format(emp.employee_id)
            result = self._execute_command(command)
            if result[0].startswith("Query OK"):
                continue
            # TODO: Error handling

    def _execute_command(self, command):
        """
        executes an sql command on the database. does NOT protect against SQL
        injection.
        """
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