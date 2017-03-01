import datetime

class Person:
    def __init__(self, gender, bmi, birthday, age):
        self.gender = gender
        self.bmi = bmi
        self.birthday = birthday
        self.age = age

    def __str__(self):
        gender_string = {"m":"Male", "f":"Female"}[self.gender.lower()]
        return "{} Person with bmi {}; {} years old".format(gender_string, self.bmi, self.age)


class Employee(Person):
    def __init__(self, employee_id, gender, sales, bmi, salary, birthday, age):
        Person.__init__(self, gender, bmi, birthday, age)
        self.employee_id = employee_id
        self.sales = sales
        self.salary = salary

    def __str__(self):
        return Person.__str__(self) + "; Employee with id {}".format(self.employee_id)


# testing functionality
bd = datetime.datetime(1995, 10, 14)
a = Employee("empID", "m", 999, 88, 77, bd, 21)
print(a)

