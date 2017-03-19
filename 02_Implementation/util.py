"""
this module offers miscellaneuos functionality that could not be put anywhere
else
"""

# python imports
import datetime
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
    """
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def exit():
    IOHelper.stdOut("Exiting program. Goodbye.")
    sys.exit()

if __name__ == "__main__":
    split = sys.argv[1].split("-")
    bday = datetime.date(int(split[0]), int(split[1]), int(split[2]))
    print(calculate_age(bday))