from datetime import datetime

class Emploee(object):
    def __init__(self, id, gender, age, sales, bmi='normal', salary, birthday = datetime.date.today()):
        self.id = id
        self.gender = gender
        self.age = age
        self.sales = sales
        self.BMI = bmi
        self.salary = salary
        self.birthday = birthdays
        
    def __str__(self):
        return 'i am a ' + self.gender + ' and I say ' + self.words
    #def speak(self):
    #    print self.words



        
        
