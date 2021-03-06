"""
this module acts as a facade to dataHandlerFile.py and dataHandlerDatabase.py
input and ouput goes to/ comes from both sources.
though redundant, this is okay in the context of the assignment.

this module cannot be tested using doctest or unit test because results change
with the state of the data source
"""

# python imports

# project imports
import dataHandlerFile as file
import dataHandlerDatabase as db
import dataHandlerSerial as ser

sources = {"db": db.DataHandlerDatabase(),
            "csv": file.DataHandlerFile(),
            "ser": ser.DataHandlerSerial()}

def get_all_employees(source):
    """
    reads all employees and returns them in a list
        @params:
            source: String describing datasource ("db" or "csv")
        @return:
            list of employee objects, may be empty
    """
    return sources[source].get_all_employees()

def get_employee(emp_id, source):
    return sources[source].get_employee(emp_id)

def employee_exists(emp_id, source):
    """
    checks whether an employee with the supplied id exists in the supplied
    datasource
    @params:
        emp_id: the four digit employee id to check
        source: String describing datasource ("db" or "csv")
    @return:
        True if an employee with the id exists, otherwise False 
    """
    return sources[source].employee_exists(emp_id)

def save_employees(employees, source):
    """
    saves the supplied employees to the supplied datasource
    @params:
        employees: list of Employee objects to save
        source: String describing datasource ("db" or "csv")
    @return: -
    """
    sources[source].save_employees(employees)

def save_employee(employee, source):
    """
    saves the supplied employee to the supplied datasource
    @params:
        employee: the Employee object to save
        source: String describing datasource ("db" or "csv")
    @return: -
    """
    save_employees([employee], source)

def update_employee(employee, source):
    sources[source].update_employee(employee)

def delete_employees(employee_ids, source):
    sources[source].delete_employees(employee_ids)

def get_statistic(statistic, group, source):
    return sources[source].get_statistic(statistic, group)

def sync_datasources():
    """
    synchronises the contents of the database and the file by copying employees
    that do not exist in one datasource from the other
    @params: -
    @return: -
    """
    raise NotImplementedError
    file_employees = file.get_all_employees()
    db_employees = db.get_all_employees()

    to_put_file = []
    to_put_db = []

    for emp_file, emp_db in zip(file_employees, db_employees):
        if not db.employee_exists(emp):
            to_put_db.append(emp)
        if not file.employee_exists(emp):
            to_put_file.append(emp)

    db.save_employees(to_put_db)
    file.save_employees(to_put_file)