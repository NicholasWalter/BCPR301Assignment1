import datetime

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