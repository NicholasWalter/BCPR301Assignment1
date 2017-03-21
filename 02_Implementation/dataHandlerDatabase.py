"""
this module offers the DataHandlerDataBase class, opening connections to a
MySQL database to save and read employees to and from.

This does NOT protect against SQL injection at all

this module cannot be tested using doctest or unit test because results change
with the state of the data source
"""

# python imports
from datetime import date
import pymysql

# project imports
from dataHandlerAbstract import DataHandlerAbstract
import employee
import inputConverter as IC
import IOHelper as IO

class DataHandlerDatabase(DataHandlerAbstract):
    
    def __init__(self, db_ip = "localhost", db_username = "pyaccess", 
                    db_password = "bcpr301", db = "bcpr301_assignment1"):
        DataHandlerAbstract.__init__(self)
        self.db_ip = db_ip
        self.db_username = db_username
        self.db_password = db_password
        self.db = db
        if not self._test_connection():
            e = "Connection to database at {} could not be established."
            raise ConnectionError(e.format(self.db_ip))

    def _test_connection(self):
        try:
            test_result = self._execute_command('SELECT test FROM connection_test')
        except:
            return False
        return True

    def get_all_employees(self):
        command = "SELECT * FROM employees"
        lines = self._execute_command(command)

        employees = []

        for l in lines:
            try:
                parameters = {}
                parameters["empid"] = IC.convert_input(l[0], "empid")
                parameters["gender"] = IC.convert_input(l[1], "gender")
                parameters["age"] = IC.convert_input(l[2], "age")
                parameters["sales"] = IC.convert_input(l[3], "sales")
                parameters["bmi"] = IC.convert_input(l[4], "bmi")
                parameters["salary"] = IC.convert_input(l[5], "salary")
                parameters["birthday"] = IC.convert_input(l[6], "birthday")
                employees.append(employee.create_employee(parameters))
            except Exception as err:
                IO.stdErr("Error in translating database row: " + str(l))
                IO.stdErr(str(err))
                print(parameters)
        return employees
    
    def save_employees(self, employees):
        c = 'INSERT INTO employees VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}")'
        for e in employees:
            command = c.format(e.employee_id, e.gender, e.age, e.sales, e.bmi,
                                e.salary, e.get_birthday_string())
            try:
                self._execute_command(command)
            except Exception as err:
                IO.stdErr("There was an error deleting employee {}".format(id))
                print(str(err))
    
    def update_employee(self, emp):
        c = 'UPDATE employees SET gender = "{}", age = {}, sales = {},' \
            + ' bmi = "{}", salary = {}, birthday = "{}" WHERE id ="{}"'
        command = c.format(emp.gender, emp.age, emp.sales,
                            emp.bmi, emp.salary, emp.birthday, emp.employee_id)
        try:
            self._execute_command(command)
        except Exception as err:
            IO.stdErr("There was an error deleting employee {}".format(id))
            print(str(err))

    def delete_employees(self, employee_ids):
        c = 'DELETE FROM employees WHERE id="{}"'
        for id in employee_ids:
            command = c.format(id)
            try:
                self._execute_command(command)
            except Exception as err:
                IO.stdErr("There was an error deleting employee {}".format(id))
                print(str(err))

    def _execute_command(self, command):
        """
        executes an sql command on the database. does NOT protect against SQL
        injection.
        """
        db = pymysql.connect(self.db_ip, self.db_username, self.db_password,
                                self.db)
        output = []
        cursor = db.cursor()

        try:
            cursor.execute(command)
            db.commit()
            line = cursor.fetchone()
            while not line is None:
                output.append(line)
                line = cursor.fetchone()
        except Exception as err:
            db.rollback()
            raise err
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