from validator import Validator
from serialization import Serialization
from graphy_display import Bar_chart


class Controller(object):

    """ docstring for Controller"""

    def __init__(self, view, model):
        self.__view = view
        self.model = model
        self.validator = Validator()
        self.serialization = Serialization()
        self.bar_chart = Bar_chart()

    def test(self, data):
        self.display_bar()

    def new_employee(self):
        input_data = dict(self.input_employee_id())
        input_data.update(self.input_birthday())
        input_data.update(self.input_gender())
        input_data.update(self.input_age())
        input_data.update(self.input_sales())
        input_data.update(self.input_BMI())
        input_data.update(self.input_salary())
        self.model.add_the_employee(input_data)
        self.__view.show(input_data)

    def load_file(self, path):
        try:
            f = open(path, "r")
            lines = [line.rstrip('\n') for line in f]
            print(lines)
            for the_line in lines:
                if self.validator.is_load_data(the_line):
                    array = the_line.split(',')
                    d = self.convert_dict("EMPID", array[0])
                    d.update(self.convert_dict("Gender", array[1]))
                    d.update(self.convert_dict("Age", array[2]))
                    d.update(self.convert_dict("Sales", array[3]))
                    d.update(self.convert_dict("BMI", array[4]))
                    d.update(self.convert_dict("Salary", array[5]))
                    d.update(self.convert_dict("Birthday", array[6]))
                    the_employee = self.model.add_the_employee(d)
                else:
                    print("invalid data")
            f.close()
        except IOError:
            self.__view.show('error : wrong path')

    def save_file(self, path):
        try:
            f = open(path, "w+")
            for employee in self.model.employees:
                f.write(employee.__str__())
                f.write('\n')
                # f.truncate()
            f.close()
        except IOError:
            self.__view.show('error : wrong path')

    def convert_dict(self, key, string):
        d = dict({key: string})
        return d

    def serialise_objects(self, path):
        try:
            if self.model.employees.__len__() == 0:
                path += '/data.pickle'
                sf = self.serialization.open(path, "wb")
                for employee in self.model.employees:
                    self.serialization.dump(sf, employee)
                sf.close()
                sf = self.serialization.open(path, "rb")
                print(self.serialization.load(sf))
                print(self.serialization.load(sf))
                print(self.serialization.load(sf))
                print(self.serialization.load(sf))
                self.serialization.close(sf)
                self.__view.show("success")
            else:
                raise ValueError
        except IOError:
            self.__view.show('error : wrong path')
        except ValueError:
            self.__view.show('data error')

    def display_bar(self):
        try:
            if(self.model.get_all_salaries().__len__() != 0):
                self.bar_chart.title = 'Salary by Age'
                self.bar_chart.add('Salary', self.model.get_all_salaries())
                self.bar_chart.x_labels = map(int, self.model.get_all_age())
                #self.bar_chart.render_to_png('/tmp/chart.png')
                self.bar_chart.render_to_file('bar_chart.svg')
                self.bar_chart.show_in_chrome('bar_chart.svg')
            else:
                raise ValueError
        except ValueError:
            self.__view.show('system has not data')

    def db_save(self):
        try:
            llist = []
            for employee in self.model.employees:
                llist.append(employee.__str__())
            self.__view.show(llist)
        except Exception as e:
            self.__view.show(e)
        # except ValueError:
        #     self.__view.show('error')

    # def db_load(self):
        # try:

        # except Exception as e:
        #     self.__view.show((e)
        # except ValueError:
        #     self.__view.show('error')

    def input_employee_id(self):
        while True:
            try:
                input_data=self.__view.input("Please input employee ID : ")
                if self.validator.is_valid_employee_id(input_data):
                    break
                else:
                    self.__view.show("That was no valid id.  Try again...")
            except ValueError:
                self.__view.show(
                    "Oops!  That was no valid number.  Try again...")
        return {"EMPID": input_data}

    def input_gender(self):
        while True:
            try:
                input_data=self.__view.input("Please input gender M/F : ")
                if self.validator.is_valid_gender(input_data):
                    break
                else:
                    self.__view.show("That was no valid input.  Try again...")
            except ValueError:
                self.__view.show(
                    "Oops!  That was no valid number.  Try again...")
        return {"Gender": input_data}

    def input_age(self):
        while True:
            try:
                input_data=self.__view.input("Please input two digit age : ")
                if self.validator.is_valid_age(input_data):
                    break
                else:
                    self.__view.show("That was no valid input.  Try again...")
            except ValueError:
                self.__view.show(
                    "Oops!  That was no valid number.  Try again...")
        return {"Age": input_data}

    def input_sales(self):
        while True:
            try:
                input_data=self.__view.input(
                    "Please input three digit sales : ")
                if self.validator.is_valid_sales(input_data):
                    break
                else:
                    self.__view.show("That was no valid input.  Try again...")
            except ValueError:
                self.__view.show(
                    "Oops!  That was no valid number.  Try again...")
        return {"Sales": input_data}

    def input_BMI(self):
        options=['Normal', 'Overweight', 'Obesity', 'Underweight']
        for (i, item) in enumerate(options):
            self.__view.show(i + 1, item)
        while True:
            try:
                input_data=int(
                    self.__view.input("Please select the BMI number:"))
                if input_data >= 1 and input_data <= 4:
                    input_data=options[input_data - 1]
                if self.validator.is_valid_BMI(input_data):
                    break
                else:
                    self.__view.show("That was no valid input.  Try again...")
            except ValueError:
                self.__view.show(
                    "Oops!  That was no valid number.  Try again...")
        return {"BMI": input_data}

    def input_salary(self):
        while True:
            try:
                input_data=self.__view.input(
                    "Please input the 2or3 digit salary : ")
                if self.validator.is_valid_salary(input_data):
                    break
                else:
                    self.__view.show("That was no valid input.  Try again...")
            except ValueError:
                self.__view.show(
                    "Oops!  That was no valid number.  Try again...")
        return {"Salary": input_data}

    def input_birthday(self):
        prompt="Please input the birthday day-month-year : "
        while True:
            try:
                input_data=self.__view.input(prompt)
                if self.validator.is_valid_birthday(input_data):
                    break
                else:
                    self.__view.show("That was no valid input.  Try again...")
            except ValueError:
                self.__view.show(
                    "Oops!  That was no valid number.  Try again...")
        return {"Birthday": input_data}
