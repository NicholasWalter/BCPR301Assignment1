"""
handles the conversion of user input and data read from database to the
appropriate data type

conversion functions may throw a ValueError if the input is valid
"""

# python imports
import datetime

# project imports
import inputValidator


def convert_input(input, input_type):
    """
    converts arbitrary string input to the appropriate format
    @params:
        input: String input to convert
        input_type: the type of input to convert
            Use "empid", "gender", "age", "sales", "salary", "bday"
    """
    converters = {"empid": convert_employee_id, "gender": convert_gender,
                    "age": convert_age, "bmi": convert_bmi,
                    "sales": convert_sales, "salary": convert_salary,
                    "bday": convert_birthday}
    if not input_type in converters:
        raise ValueError("Use one of the following types: " +
                            str(list(converters.keys())))
    try:
        return converters[input_type](input)
    except ValueError as err:
        raise err

def convert_employee_id(employee_id):
    if not inputValidator.validate_input_employee_id(employee_id):
        raise ValueError("Input for employee id invalid: {}".format(employee_id))
    return employee_id.upper()

def convert_gender(gender):
    if not inputValidator.validate_input_gender(gender):
        raise ValueError("Input for ǵender invalid: {}".format(gender))
    return gender.lower()

def convert_age(age):
    if not inputValidator.validate_input_age(age):
        raise ValueError("Input for age invalid: {}".format(age))
    return int(age)

def convert_bmi(bmi):
    if not inputValidator.validate_input_bmi(bmi):
        raise ValueError("Input for BMI invalid: {}".format(bmi))
    return bmi.lower()

def convert_sales(sales):
    if not inputValidator.validate_input_sales(sales):
        raise ValueError("Input for sales invalid: {}".format(sales))
    return int(sales)

def convert_salary(salary):
    if not inputValidator.validate_input_salary(salary):
        raise ValueError("Input for salary invalid: {}".format(salary))
    return int(salary)

def convert_birthday(birthday):
    if not inputValidator.validate_input_birthday(birthday):
        raise ValueError("Input for birthday invalid: {}".format(birthday))
    split = birthday.split("-")
    year = int(split[0])
    month = int(split[1])
    day = int(split[2])
    return datetime.date(year, month, day)