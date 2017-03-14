import datetime


class Person:
    def __init__(self, gender, bmi, birthday, age):
        self.gender = gender
        self.bmi = bmi
        self.birthday = birthday
        self.age = age

    def __str__(self):
        gender_string = {"m": "Male", "f": "Female"}[self.gender.lower()]
        return "{} person, born {} ({}); bmi: {}".format(gender_string,
                            self._get_birthday_string(),
                            self.age, self.bmi)

    def _get_birthday_string(self):
        bday = self.birthday
        return "{}-{}-{}".format(bday.year, bday.month, bday.day)


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
        return "ID {}: Sales: {} Salary: {}".format(self.employee_id,
                                                    self.sales,
                                                    self.salary) \
                                                    + " " \
                                                    + Person.__str__(self)

    def equals(self, other):
        """
        checks whether this Employee object and the supplied other are identical
        @params:
            self: this object
            other: another Employee object
        """
        # using and instead of && to make use of short circuiting
        return self.employee_id == other.employee_id and \
                self.gender == other.gender and \
                self.sales == other.sales and \
                self.bmi == other.bmi and \
                self.salary == other.salary and \
                self.birthday == other.birthday and \
                self.age == other.age

    def get_csv_line(self):
        return "{},{},{},{},{},{},{}\n".format(self.employee_id, self.gender,
                                                self.sales, self.bmi,
                                                self.salary,
                                                self._get_birthday_string(),
                                                self.age)

def create_employee(attributes):
    """
    creates an employee using the supplied data
    @params:
        attributes: dict containing attributes of employees to create
        must contain: "empid", "gender", "sales", "bmi", salary", "birthday",
        "age"
    @return:
        new Employee object
    @raises:
        ValueError if the supplied dict did not contain one of the required
        attributes
    """
    neccessary_keys = ["empid", "gender", "sales", "bmi", "salary", "birthday",
                        "age"]
    for key in neccessary_keys:
        if not key in attributes.keys():
            raise ValueError("employee could not be created: {} is missing".format(key))
    return Employee(attributes["empid"], attributes["gender"],
                    attributes["sales"], attributes["bmi"],
                    attributes["salary"], attributes["birthday"],
                    attributes["age"])