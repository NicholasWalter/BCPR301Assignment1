"""
this module offers the DataHandlerAbstract class, bundling functionality that
both DataHandlerFile and DataHandlerDatabase need.
"""

class DataHandlerAbstract:
    """
    this is an abstract class to define the interface of all DataHandler
    classes.
    """

    def __init__(self):
        pass

    def get_statistic(statistic, group):
        raise NotImplementedError

        all_employees = self.get_all_employees()

        # TODO: LOW: redo with list comprehensions

        step1 = {}
        for emp in all_employees:
            this_group = getattr(emp, group)
            this_value = getattr(emp, statistic)
            if not this_group in step1.keys():
                step1[this_group] = [0, 0]
            previous_value = step1[this_group]
            new_value = [previous_value[0] + this_value, previous_value[1] + 1]
            step1[this_group] = new_value

        step2 = {}
        for group in step1:
            record = step1[group]
            step2[group] = record[0] / record[1]

        return step2

# TODO: MEDIUM: refacotr using abstract base class/ metaclass