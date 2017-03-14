"""
handles the validation of user input and data read from database. Each function
will return True if the input is valid, otherwise False
"""

import datetime

def validate_input(input, input_type):
    validators = {"empid": validate_input_employee_id,
                    "gender": validate_input_gender,
                    "age": validate_input_age,
                    "bmi": validate_input_bmi,
                    "sales": validate_input_sales,
                    "salary": validate_input_salary,
                    "birthday": validate_input_birthday}
    return validators[input_type](input)

def validate_input_employee_id(employee_id_input):
    """
    checks whether the supplied input is in the correct format
    correct format is [A-Z][0-9]{3} e.g. A123
    @params:
        employee_id_input: String to check
    @return:
        True if the input is valid, otherwise False
    """
    if len(employee_id_input) != 4:                     # must be 4 digits long
        return False
    first_digit = employee_id_input[0].upper()
    rest = employee_id_input[1:]
    if not ord(first_digit) in range(65,91):            # first digits must be letter
        return False
    try:
        a = int(rest)                                   # digits 2-4 must be integer
    except:
        return False
    return True

def validate_input_gender(gender_input):
    """
    checks whether the supplied input is valid
    valid input is either "m" or "f" in upper or lower case
    @params:
        gender_input: String to check
    @return:
        True if the input is valid, otherwise False
    """
    return gender_input in ["M", "F", "m", "f"]         # can be "m" or "f" in upper or lower

def validate_input_age(age_input):
    """
    checks whether the supplied age input is valid
    valid are all integers between 00 and 99
    @params:
        age_input: String to check
    @return:
        True if the input is valid, otherwise False
    """
    return True in [_valid_input_integer(age_input, i) for i in range(1, 3)]

def validate_input_bmi(bmi_input):
    """
    checks whether the supplied bmi input is valid
    valid inputs are "normal", "overweight", "obesity" and "underweight"
    in upper or lower case
    @params:
        bmi_input: String to check
    @return:
        True if the input is valid, otherwise False
    """
    return bmi_input.lower() in ["normal", "overweight", "obesity",
                                    "underweight"]

def validate_input_sales(sales_input):
    """
    checks whether the supplied sales input is valid
    valid are all integers between 000 and 999
    @params:
        sales_input: String to check
    @return:
        True if the input is valid, otherwise False
    """
    return True in [_valid_input_integer(sales_input, i) for i in range(1, 4)]

def validate_input_salary(salary_input):
    """
    checks whether the supplied salary input is valid
    valid are all integers between 00 and 99 as well as between 000 and 999
    @params:
        salary_input: String to check
    @return:
        True if the input is valid, otherwise False
    """
    return True in [_valid_input_integer(salary_input, i) for i in range(1, 4)]

def validate_input_birthday(birthday_input):
    """
    checks whether the supplied birthday input is valid
    valid birthdays consist of day, month and year
    @params:
        birthday_input
    """
    split = birthday_input.split("-")
    if len(split) != 3:                                 # should be 3 parts to this
        return False
    day = split[0]
    month = split[1]
    year = split[2]
    try:                                                # should all be integers
        day_int = int(day)
        month_int = int(month)
        year_int = int(year)
    except:
        return False
    if day_int not in range(1, 32):                     # day should be 1 to 31
        return False
    if month_int not in range(1, 13):                   # month should be 1 to 12
        return False
    if year_int not in range(0, 10000):                 # year should be 0 to 9999
        return False
    try:                                                # check if this is a valid date (e.g. not feb 31)
        a = datetime.datetime(year_int, month_int, day_int)
    except:
        return False
    return True

def validate_input_age_and_birthday(birthday, age):
    today = datetime.date.today()
    return age == today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def _valid_input_integer(integer_input, digits):
    """
    checks whether the supplied input is an integer with the supplied number of digits
    @params:
        integer_input: String to check
        digits: the number of digits the input may have
    """
    if len(integer_input) != digits:
        return False
    try:
        a = int(integer_input)
    except:
        return False
    return True

################################################################################
## Testing functionality                                                      ##
################################################################################

def test_input_integer():
    print("testing inputValidator._valid_input_integer()")
    test_cases = [0, 1000, 99, 999]
    for i in test_cases:
        pass