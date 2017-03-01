import datetime


class Person:
    def __init__(self, gender, bmi, birthday, age):
        self.gender = gender
        self.bmi = bmi
        self.birthday = birthday
        self.age = age

    def __str__(self):
        gender_string = {"m": "Male", "f": "Female"}[self.gender.lower()]
        return "{} Person with bmi {}; {} years old".format(gender_string, self.bmi, self.age)


class Employee(Person):
    """
    defines the dataset of an employee. inherits from Person.
    should only be used with validated inputs (see util.py module)
    @params:
        employee_id: the employee's id, should be [A-Z][0-]{3}
        gender: should be "m" or "f"
        sales: should be integer 0-99
        bmi: should be "normal", "overweight", "obesity" or "underweight"
        salary: should be integer 0-999
        birthday: should be datetime object
        age: should be integer age in years
    """
    def __init__(self, employee_id, gender, sales, bmi, salary, birthday, age):
        Person.__init__(self, gender, bmi, birthday, age)
        self.employee_id = employee_id
        self.sales = sales
        self.salary = salary

    def __str__(self):
        return Person.__str__(self) + "; Employee with id {}".format(self.employee_id)


# testing functionality
def test():
    bd = datetime.datetime(1995, 10, 14)
    a = Employee("empID", "m", 999, "normal", 77, bd, 21)
    print(a)

if __name__ == "__main__":
    test()
