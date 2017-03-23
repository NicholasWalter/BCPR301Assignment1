"""
this module offers the Employee (and Person) class. They can be used to store
information about an employee in a convenient way.
"""

# python imports
import datetime
import doctest


class Person():
    def __init__(self, gender, bmi, birthday, age):
        self.gender = gender
        self.bmi = bmi
        self.birthday = birthday
        self.age = age

    def __str__(self):
        gender_string = {"m": "Male", "f": "Female"}[self.gender.lower()]
        return "{} person, born {} ({}); bmi: {}".format(gender_string,
                            self.get_birthday_string(),
                            self.age, self.bmi)

    def get_birthday_string(self):
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
            self:
                this object
            other:
                another Employee object
        @return:
            True if the other employee is the same as this, otherwise False
        >>> bd1 = datetime.date(1990, 1, 1)
        >>> bd2 = datetime.date(1990, 1, 2)
        >>> this = Employee("A123", "m", 999, "normal", 999, bd1, 21)
        >>> equal = Employee("A123", "m", 999, "normal", 999, bd1, 21)
        >>> different = Employee("B234", "f", 0, "obesity", 0, bd2, 99)
        >>> this.equals(equal)
        True
        >>> this.equals(different)
        False
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
        """
        gets the line used to save the information for this employee in a csv
        file
        @params: -
        @return:
            the csv line for this employee
        >>> bd = datetime.date(1990, 1, 1)
        >>> emp = Employee("A123", "m", 999, "normal", 999, bd, 21)
        >>> a = emp.get_csv_line()
        >>> a.startswith('A123,m,999,normal,999,1990-1-1,21')
        # THIS FUCKING POS
        # result comes with \n at the end
        # cannot add \n AT THE END OF THE STRING because it interprets it in the
        # code AND CRASHES OBVIOUSLY. FUCK this doctest stuff.
        True
        """
        return "{},{},{},{},{},{},{}\n".format(self.employee_id, self.gender,
                                                self.sales, self.bmi,
                                                self.salary,
                                                self.get_birthday_string(),
                                                self.age)

def create_employee(attributes):
    """
    creates an employee using the supplied data
    @params:
        attributes:
            dict containing attributes of employees to create
            must contain: "empid", "gender", "sales", "bmi", salary",
            "birthday", "age"
    @return:
        new Employee object
    @raises:
        ValueError if the supplied dict did not contain one of the required
        attributes
    >>> bd = datetime.date(1990, 1, 1)
    >>> good_attr = {"empid": "A123", "gender": "m", "sales": 999, "bmi": "normal", "salary": 999, "birthday": bd, "age": 21}
    >>> bad_attr = {"empid": "A123", "gender": "m", "sales": 999, "bmi": "normal", "salary": 999, "birthday": bd}
    # cannot split lines here because FUCKING DOCTEST is gonna FUCKING CRASH
    >>> gemp = create_employee(good_attr)
    >>> bemp = create_employee(bad_attr)
    Traceback (most recent call last):
        ...
    ValueError: employee could not be created: age is missing
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

if __name__ == "__main__":
    print("testing employee.py")
    doctest.testmod()