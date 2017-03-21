"""
this module offers a command line interface to the functionality of the program.

Considering the scope of the project, all data read will be read directly from
the datasources every time it is accessed. In a larger scale product, this would
obviously harm performance.
Furthermore nothing in here is safe to be used by multiple users simultaneously.

Nothing in here can be tested as it is only an interface to user commands.
"""

# python imports
from cmd import Cmd
import os
import sys

# project imports
from administratorAbstract import AdministratorAbstract
import charts as GUI
import dataHandlerFacade as dataHandler
import dataHandlerFile
import employee
import inputConverter as IC
import inputValidator as IV
import util


class AdministratorCMD(Cmd, AdministratorAbstract):
    """
    """
    def __init__(self):
        Cmd.__init__(self)
        AdministratorAbstract.__init__(self)
        self.prompt = "> "
        self.my_name = "Employee administration program"
        self._datasource = "csv"
        self._print_welcome()

    def _print_welcome(self):
        print("\n\n")
        print("Welcome to the employee administration program.")
        print("Use \"help\" to get an overview over the available commands")
        print("\nNote: By default, the datasource is set to csv.")

    def do_exit(self, line):
        """
        Syntax: exit
        Terminates the application
        parameters: -
        output: -
        """
        print("Application terminated. Goodbye.")
        return True

    def do_datasource(self, line):
        """
        Syntax: datasource [datasource]
        Sets the current datasource to the specified item.

        At startup, the datasource is set to "csv" per default.

        parameters:
            datasource:
                Use "db" to set to the default database.
                Use "csv" to use the default csv file
                Leave empty to print the current datasource
        output:
            A confirmation message
        """
        if len(line) == 0:
            print("Current datasource: " + self._datasource)
            return False
        if not line in ["csv", "db", "ser"]:
            self.do_help("list")
            return False    
        self._datasource = line

    def do_list(self, line):
        """
        Syntax: list [datasource]
        Lists all employees saved by the application
        parameters:
            datasource:
                select "db" or "csv" to list employees in the
                database or in the csv file. leave empty to use both
        output:
            a list of employees from the specified sources. employee ids may
            appear more than once if the same employee is saved in more than
            one data source with different attributes.
        """
        try:
            emps = dataHandler.get_all_employees(self._datasource)
        except ConnectionError as cerr:
            err = str(cerr) + " Please check your network connection"
            self.stdErr(err)
            return False
        except FileNotFoundError as ferr:
            err = str(ferr) + " Please ensure that the file is accessible."
            self.stdErr(err)
            return False
        [print(e) for e in emps]

    def do_add_employee(self, line):
        """
        Syntax: add_employee [employee id]
        Starts the process to add a new employee to the current datasource
        parameters:
            employee id:
                the four digit id of the employee to update. may not exist in
                the datasource yet, must be 1 letter and three numbers, e.g.
                "A123"
        output:
            after the process is finished, all information about the new
            employee is displayed
        """
        if not IV.validate_input_employee_id(line):
            self.do_help("add_employee")
            return False

        new_emp_id = line

        if dataHandler.employee_exists(new_emp_id, self._datasource):
            print("An employee with this id already exists.")
            return False

        inputs = {"gender": "gender",
                        "sales": "sales performance (0-999)",
                        "bmi": "bmi (normal, overweight, obesity, underweight)",
                        "salary": "salary (0-999)",
                        "birthday": "birthday (dd-mm-yyyy)",
                        "age": "age (0-99)"}
        
        prompt = "Please enter the new employee's {}: "

        for k in inputs.keys():
            val = input(prompt.format(inputs[k]))
            while not IV.validate_input(val, k):
                print("There was an error. Please check your input.")
                val = input(prompt.format(inputs[k]))
            inputs[k] = IC.convert_input(val, k)

        inputs["empid"] = new_emp_id

        new_emp = employee.create_employee(inputs)

        dataHandler.save_employee(new_emp, self._datasource)

    def do_read_csv_file(self, line):
        """
        Syntax: read_file [path] [target]
        Reads the supplied csv file and saves all contained Employees to the
        supplied target. If an employee already exists in the target, it will
        be updated
        parameters:
            path:
                full path to the file to read
            target:
                use "db" to save in database, "csv" to save in csv file,
                "ser" to serialize and save the employees
        output:
            A description for any error in the reading/ saving process
        """
        split = line.split(" ")
        # check input
        if not len(split) == 2:
            print("invalid parameters: " + line)
            self.do_help("read_csv_file")
            return False
        if not split[1] in ["db", "csv", "ser"]:
            print("invalid target parameter. use \"db\", \"csv\" or \"ser\"")
            return False
        try:
            handler = dataHandlerFile.DataHandlerFile(split[0])
        except FileNotFoundError:
            print("could not find file \"{}\", skipping.".format(split[0]))
            return False

        print("Reading csv file: {}".format(split[0]))
        # read employees from source file
        all_employees = handler.get_all_employees()
        to_save = []

        # update employees in target if they already exist
        for emp in all_employees:
            if dataHandler.employee_exists(emp.employee_id, split[1]):
                dataHandler.update_employee(emp, split[1])
            else:
                to_save.append(emp)

        # save employees that do not yet exist in target
        dataHandler.save_employees(to_save, split[1])

    def do_update_employee(self, line):
        """
        Syntax: update_employee [employee id]
        Starts the update process for the employee with the selected id
        parameters:
            employee id:
                the four digit id of the employee to update
        output:
            after the process is finished, all old and new information about the
            employee is displayed
        """
        if not IV.validate_input_employee_id(line):
            print("invalid employee id.")
            self.do_help("update_employee")
            return False
        if not dataHandler.employee_exists(line, self._datasource):
            print("employee does not exist.")
            return False
        to_change = dataHandler.get_employee(line, self._datasource)
        print("The employee to change:")
        print(to_change)
        print("If you want to change an attribute, please enter the new value")
        print("To leave an attribute unchanged, leave prompt empty")
        attributes = ["gender", "sales", "bmi", "salary", "birthday", "age"]

        prompt = "Attribute: {} Current: {} Enter new value:\n"
        for a in attributes:
            uin = "XXXXX"
            skip = False
            while not IV.validate_input(uin, a):
                if len(uin) == 0:
                    skip = True
                    break
                uin = input(prompt.format(a, getattr(to_change, a)))
            if not skip:
                uin = IC.convert_input(uin, a)
                setattr(to_change, a, uin)

        print("Updated employee:")
        print(to_change)
        uin = "X"
        while not uin.lower() in ["y", "n"]:
            uin = input("Do you want to accept these changes (y/n)")
        if uin == "y":
            dataHandler.update_employee(to_change, self._datasource)


    def do_delete_employees(self, line):
        """
        Syntax: delete_employees [employee id] [employee id] [...]
        Deletes the employees identified by the specified employee ids from the
        current datasource.
        parameters:
            employee id (may be more than one):
                the four digit ids of the employees to delete
        output:
            list of employees that were deleted
        """
        split = line.split(" ")
        if len(split) < 1:
            self.do_help("delete_employees")
            return False
        checked = [i for i in split if IV.validate_input(i, "empid")]
        [print("Invalid employee id: {}".format(a)) for a in split \
        if not a in checked]
        dataHandler.delete_employees(checked, self._datasource)

    def do_get_info(self, line):
        """
        Syntax: get_info
        Displays information about the system and the available default data
        sources
        """
        datasources = {"db": "Database", "csv": "CSV File",
                        "ser": "Serialization"}
        for ds in datasources.keys():
            descr = datasources[ds]
            try:
                print("Information about {}:".format(descr))
                all_employees = dataHandler.get_all_employees(ds)
                count = len(all_employees)
                print("{} employees saved in this data source".format(count))
                print()
            except:
                print("Error when fetching information about {}".format(descr))

    def do_get_statistic(self, line):
        """
        Syntax: get_statistic [parameter] [group]
        Displays the selected parameter grouped by the selected group.
        e.g. "get_statistic salary gender" will display the total and average
        salary for male and female employees.
        parameters:
            parameter:
                the parameter to examine (may be "sales", "salary", "age")
            group:
                the parameter to group results by (me be "gender", "sales",
                "bmi", "salary", "birthday", "age")
        output:
            a window showing the statistic
        """
        if len(line.split(" ")) != 2:
            print("invalid parameters.")
            self.do_help("get_statistic")
            return False
        valid_parameters = ["sales", "salary", "age"]
        valid = ["gender", "sales", "bmi", "salary", "birthday", "age"]
        split = line.split(" ")
        if split[0] not in valid_parameters or split[1] not in valid:
            print("invalid parameters.")
            self.do_help("get_statistic")
            return False
        result = dataHandler.get_statistic(split[0], split[1], self._datasource)
        GUI.display_statistic(result, split[0], split[1])

    def cmdloop(self, args):
        # TODO: high: read params from line & import employees
        if len(args) > 0:
            for item in args:
                if item.endswith(".csv"):
                    self.do_read_csv_file(item + " csv")
                else:
                    print('invalid parameter: "{}", skipping'.format(item))
        Cmd.cmdloop(self)

    def stdOut(self, msg):
        print(msg)

    def stdErr(self, msg):
        print(msg)

instance = None

def start(args, new_instance):
    global instance
    instance = new_instance
    instance.cmdloop(args)