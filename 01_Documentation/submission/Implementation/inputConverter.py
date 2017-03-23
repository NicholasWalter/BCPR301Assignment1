"""
handles the conversion of user input and data read from database to the
appropriate data type

conversion functions may throw a ValueError if the input is valid
"""

# python imports
import datetime
import doctest

# project imports
import inputValidator


def convert_input(input, input_type):
    """
    converts arbitrary string input to the appropriate format
    since all functionality is borrowed from other functions, no testing needed
    @params:
        input: String input to convert
        input_type: the type of input to convert
            Use "empid", "gender", "age", "sales", "salary", "bday"
    """
    converters = {"empid": convert_employee_id, "gender": convert_gender,
                    "age": convert_age, "bmi": convert_bmi,
                    "sales": convert_sales, "salary": convert_salary,
                    "birthday": convert_birthday}
    if not input_type in converters:
        raise ValueError("Invalid input type: {}. Use one of the following types: "
                            .format(input_type) +
                            str(list(converters.keys())))
    try:
        return converters[input_type](input)
    except ValueError as err:
        raise err

def convert_employee_id(employee_id):
    """
    converts the employee id input. effectively makes sure that char 1 is in 
    upper case
    @params:
        employee_id:
            the employee input to convert
    @return:
        the converted input
    >>> convert_employee_id("AAAA")
    Traceback (most recent call last):
        ...
    ValueError: Input for employee id invalid: AAAA
    >>> convert_employee_id("a123")
    'A123'
    >>> convert_employee_id("A123")
    'A123'
    """
    if not inputValidator.validate_input_employee_id(employee_id):
        raise ValueError("Input for employee id invalid: {}".format(employee_id))
    return employee_id.upper()

def convert_gender(gender):
    """
    converts the gender input. converts "male" to "m" and "female" to "f"
    @params:
        gender:
            the gender input to convert
    @return:
        the converted input
    >>> convert_gender("m")
    'm'
    >>> convert_gender("M")
    'm'
    >>> convert_gender("f")
    'f'
    >>> convert_gender("F")
    'f'
    >>> convert_gender("male")
    'm'
    >>> convert_gender("female")
    'f'
    >>> convert_gender("Error")
    Traceback (most recent call last):
        ...
    ValueError: Input for gender invalid: Error
    """
    if gender.lower() == "male":
        gender = "m"
    elif gender.lower() == "female":
        gender = "f"
    if not inputValidator.validate_input_gender(gender):
        raise ValueError("Input for gender invalid: {}".format(gender))
    return gender.lower()

def convert_age(age):
    """
    converts the age input. converts the input from string to integer
    @params:
        age:
            the age input to convert
    @return:
        the converted input
    >>> convert_age("a")
    Traceback (most recent call last):
        ...
    ValueError: Input for age invalid: a
    >>> convert_age("20")
    20
    """
    if not inputValidator.validate_input_age(age):
        raise ValueError("Input for age invalid: {}".format(age))
    return int(age)

def convert_bmi(bmi):
    """
    converts the bmi input. converts the input to lower case
    @params
        bmi:
            the bmi input to convert
    @return:
        the converted input
    >>> convert_bmi("Overweight")
    'overweight'
    >>> convert_bmi("Error")
    Traceback (most recent call last):
        ...
    ValueError: Input for BMI invalid: Error
    """
    if not inputValidator.validate_input_bmi(bmi):
        raise ValueError("Input for BMI invalid: {}".format(bmi))
    return bmi.lower()

def convert_sales(sales):
    """
    converts the sales input. converts the input to integer
    @params:
        sales:
            the sales input to convert
    @return:
        the converted input
    >>> convert_sales("999")
    999
    >>> convert_sales("9999")
    Traceback (most recent call last):
        ...
    ValueError: Input for sales invalid: 9999
    """
    if not inputValidator.validate_input_sales(sales):
        raise ValueError("Input for sales invalid: {}".format(sales))
    return int(sales)

def convert_salary(salary):
    """
    converts the salary input. converts the input to integer
    @params:
        sales:
            the salary input to convert
    @return:
        the converted input
    >>> convert_salary("999")
    999
    >>> convert_salary("9999")
    Traceback (most recent call last):
        ...
    ValueError: Input for salary invalid: 9999
    """
    if not inputValidator.validate_input_salary(salary):
        raise ValueError("Input for salary invalid: {}".format(salary))
    return int(salary)

def convert_birthday(birthday):
    """
    converts the birthday input from string to a datetime.date object
    @params:
        birthday:
            the birthday string to convert
    @return:
        the converted input as datetime.date object
    >>> convert_birthday("01-01-1990")
    datetime.date(1990, 1, 1)
    >>> convert_birthday("31-02-1990")
    Traceback (most recent call last):
        ....
    ValueError: Input for birthday invalid: 31-02-1990
    """
    if not inputValidator.validate_input_birthday(birthday):
        raise ValueError("Input for birthday invalid: {}".format(birthday))
    split = birthday.split("-")
    day = int(split[0])
    month = int(split[1])
    year = int(split[2])
    return datetime.date(year, month, day)

if __name__ == "__main__":
    print("testing inputConverter.py")
    doctest.testmod()