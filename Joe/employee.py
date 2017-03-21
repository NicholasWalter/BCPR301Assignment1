from datetime import date, datetime
#from dateutil.parser import parse


class Employee(object):

    def __init__(self, id='E123', gender='male', age=11, sales=123, bmi='normal', salary=123, birthday=date.today()):
        self.id = id
        self.gender = gender
        self.age = age
        self.sales = sales
        self.BMI = bmi
        self.salary = salary
        self.birthday = datetime.strptime(birthday, '%d-%m-%Y')

    def __str__(self):
        txt = self.id + ',' + self.gender + ',' + \
            self.age + ',' + self.sales + ','
        txt += self.BMI + ',' + self.salary + \
            ',' + self.birthday.strftime('%d-%m-%Y')
        return txt
    # def speak(self):))
    #    print self.words
