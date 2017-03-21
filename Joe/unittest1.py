import unittest

from cmd_view import CLI
from controller import Controller
from model import Model
from validator import Validator


class MainTests(unittest.TestCase):

    def setUp(self):

        # self.cli = CLI()
        self.model = Model()
        # self.ctl = Controller(self.cli, self.model)
        # self.cli.set_controller(self.ctl)
        self.v = Validator()

   # def tearDown(self):
        # be executed after each test case
        # print('down')

    def test_03(self):
        self.assertFalse(self.v.is_valid_gender("m"))

    def test_02(self):
        data = {"EMPID": "A123", "Gender": "M", "Age": "34", "Sales":
                "23", "BMI": "Normal", "Salary": "12", "Birthday": "1-1-1991"}
        self.model.add_the_employee(data)
        data = self.model.get_all_age()
        print(self.model.employees)
        self.assertEqual(data[0], 34)

    #@unittest.skip('I have not coded how this will work yet.')
    def test_01(self):
        data = {"EMPID": "A123", "Gender": "M", "Age": "34", "Sales":
                "23", "BMI": "Normal", "Salary": "12", "Birthday": "1-1-1991"}
        self.model.add_the_employee(data)
        self.assertEqual(self.model.employees.__len__(), 1)

if __name__ == '__main__':
    unittest.main(verbosity=2)  # with more details
    # unittest.main()
