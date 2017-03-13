"""
this module offers the DataHandlerAbstract class, bundling functionality that
both DataHandlerFile and DataHandlerDatabase need.
"""

# python imports
from abc import abstractmethod
import abc

class DataHandlerAbstract(metaclass=abc.ABCMeta):
    """
    this is an abstract class to define the interface of all DataHandler
    classes.
    """

    def __init__(self):
        super().__init__()
        print("DataHandlerAbstract constructor")
        pass

    def get_statistic(self, statistic, group):
        """
        creates a statistic from the saved data. e.g. calling with "salary" and
        "gender" will return a comparison of salaries for male and female
        employees

        this assumes that both statistic and group have been checked for
        validity
        @params:
            statistic:
                the statistic to examine
            group:
                the attribute to group results by
        @return:
            list containing two items:
                boolean indicating the type of result: True for result type a
                    ({group: [total, average]}), False for result type b
                    ({group: [count]})
                dictionary with groups (e.g. "m" and "f") as keys and the
                average value for statistic as value. {"m": 888, "f":999}
        """

        # TODO: LOW: redo with list comprehensions
        # TODO: HIGH: enable string stuff (e.g. bmi as statistic)

        return self._get_statistic_default(statistic, group)

    def _get_statistic_string(self, statistic, group):
        all_employees = self.get_all_employees()

        result = {}
        for emp in all_employees:
            this_group = getattr(emp, group)
            this_value = getattr(emp, statistic)
            if not this_group in result:
                result[this_group] = 0
            result[this_group] +=1

        return result


        raise NotImplementedError

    def _get_statistic_default(self, statistic, group):
        all_employees = self.get_all_employees()

        # collect total value and count
        step1 = {}
        for emp in all_employees:
            this_group = getattr(emp, group)
            this_value = getattr(emp, statistic)
            if not this_group in step1.keys():
                step1[this_group] = [0, 0]
            previous_value = step1[this_group]
            new_value = [previous_value[0] + this_value, previous_value[1] + 1]
            step1[this_group] = new_value

        # calculate averages
        step2 = {}
        for group in step1:
            record = step1[group]
            step2[group] = [record[0] / record[1], record[0]]

        return step2

    def save_employee(self, employee):
        """
        saves a single employee to the data source. calls self.save_employees()
        with the supplied Employee object in a list
        @params:
            employee: The Employee object so save
        @return: -
        """
        self.save_employees([employee])

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

    def delete_employee(self, employee):
        """
        deletes the supplied employee from the data source. calls
        self.delete_employees() with the suppplied Employee object in a list
        @params:
            employee: the Employee object to delete
        @reeturn: -
        """
        self.delete_employees([employee])

    @abstractmethod
    def get_all_employees(self):
        pass

    @abstractmethod
    def save_employees(self, employees):
        pass

    @abstractmethod
    def update_employee(self, employee):
        pass

    @abstractmethod
    def delete_employees(self, employees):
        pass