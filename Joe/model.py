from employee import Employee


class Model(object):

    """docstring for Model"""
    #cmd_view = inject.instance(CLI)

    def __init__(self):
        self.employees = []

    def add_the_employee(self, data):
        new_employee = Employee(data['EMPID'], data['Gender'], data['Age'], data[
                                'Sales'], data['BMI'], data['Salary'], data['Birthday'])
        self.employees.append(new_employee)
        print(self.employees)
        return new_employee

    def get_all_salaries(self):
        salary_list = []
        for employee in self.employees:
            salary_list.append(int(employee.salary))
        return salary_list

    def get_all_sales(self):
        sales_list = []
        for employee in self.employees:
            sales_list.append(int(employee.sales))
        return sales_list

    def get_all_age(self):
        age_list = []
        for employee in self.employees:
            age_list.append(int(employee.age))
        age_list.sort()
        return age_list