"""
this module offers miscellaneuos functionality that could not be put anywhere
else
"""

# python imports
import datetime
import doctest
import sys

# project imports
import IOHelper


def calculate_age(born):
    """
    calculates the age of a person in years based on their birthday
    @params:
        born: datetime.date or datetime.datetime object representing the
        employee's birthday
    @return:
        age of employee in years as integer        
    >>> born = datetime.date(1995, 10, 14)
    >>> calculate_age(born)
    21
    """
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def exit():
    IOHelper.stdOut("Exiting program. Goodbye.")
    sys.exit()

if __name__ == "__main__":
    print("testing util.py")
    doctest.testmod()