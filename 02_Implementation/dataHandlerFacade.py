"""
this module acts as a facade to dataHandlerFile.py and dataHandlerDatabase.py
input and ouput goes to/ comes from both sources.
though redundant, this is okay in the context of the assignment.
"""

# python imports

# project imports
import dataHandlerFile as file
import dataHandlerDatabase as db

def get_all_employees():
    """
    reads all employees and returns them in a list
        @params: -
        @return:
            list of employee objects, may be empty
    """
    file_employees = file.get_all_employees()
    db_employees = db.get_all_employees()
    
    # join the two lists
    # cannot use .extend() because the objects, while equal, are not identical
    for emp in file_employees:
        contained = False
        for emp2 in db_employees:
            if emp.equals(emp2):
                contained = True
                break
        if not contained:
            db_employees.append(emp)
    return db_employees

def employee_exists(employee):
    return True in [file.employee_exists(employee), db.employee_exists(employee)]

def save_employees(employees):
    file.save_employees(employees)
    db.save_employees(employees)

def get_statistic(statistic, group):
    raise NotImplementedError

def sync_datasources():
    """
    synchronises the contents of the database and the file by copying employees
    that do not exist in one datasource from the other
    @params: -
    @return: -
    """
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