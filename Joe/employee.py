from datetime import date, datetime
#from dateutil.parser import parse
class Employee(object):
    def __init__(self, id='E123', gender='male', age=11, sales=123, bmi='normal', salary=123, birthday = date.today()):
        self.id = id
        self.gender = gender
        self.age = age
        self.sales = sales
        self.BMI = bmi
        self.salary = salary
        self.birthday = birthday
        
    def __str__(self):
        return 'i am a ' + self.gender + ' my age is ' + self.age
    #def speak(self):
    #    print self.words



        
        
