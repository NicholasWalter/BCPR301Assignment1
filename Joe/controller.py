#
#import inject
# import string
# import sys
from validator import Validator 

class Controller(object):
	"""docstring for Controller"""
	#cmd_view = inject.instance(CLI)
	
	def __init__(self, view, model):
		self.__view = view
		self.model = model
		self.validator = Validator()
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

	# def input_employee_id(self):
	# 	result = False
	# 	while(result != True):
	# 		input_data = self.view.input("Please input employee ID : ")
	# 		if self.validator.is_valid_employee_id(input_data):
	# 			self.view.show("Valid data")
	# 			result = True
	# 		else:
	# 			self.view.show("invalid data")
	# 			result = False
	# 	return {"EMPID" : input_data}
	def input_employee_id(self):
		while True:
			 try:
			     input_data = self.__view.input("Please input employee ID : ")
			     if self.validator.is_valid_employee_id(input_data):
			     	break
			     else:
			     	self.__view.show("That was no valid id.  Try again...")
			 except ValueError:
			     self.__view.show("Oops!  That was no valid number.  Try again...")
		return {"EMPID" : input_data}
		
	def input_gender(self):
		while True:
			 try:
			     input_data = self.__view.input("Please input gender M/F : ")
			     if self.validator.is_valid_gender(input_data):
			     	break
			     else:
			     	self.__view.show("That was no valid input.  Try again...")
			 except ValueError:
			     self.__view.show("Oops!  That was no valid number.  Try again...")
		return {"Gender" : input_data}
	def input_age(self):
		while True:
			 try:
			     input_data = self.__view.input("Please input two digit age : ")
			     if self.validator.is_valid_age(input_data):
			     	break
			     else:
			     	self.__view.show("That was no valid input.  Try again...")
			 except ValueError:
			     self.__view.show("Oops!  That was no valid number.  Try again...")
		return {"Age" : input_data}
	def input_sales(self):
		while True:
			 try:
			     input_data = self.__view.input("Please input three digit sales : ")
			     if self.validator.is_valid_sales(input_data):
			     	break
			     else:
			     	self.__view.show("That was no valid input.  Try again...")
			 except ValueError:
			     self.__view.show("Oops!  That was no valid number.  Try again...")
		return {"Sales" : input_data}

	def input_BMI(self):
		options = ['Normal', 'Overweight', 'Obesity', 'Underweight']
		for (i, item) in enumerate(options):
			self.__view.show(i + 1, item)
		while True:
			 try:
			    input_data = int(self.__view.input("Please select the BMI number:"))
			    if input_data >= 1 and input_data <=4:
			    	input_data = options[input_data - 1]
			    if self.validator.is_valid_BMI(input_data):
			     	break
			    else:
			     	self.__view.show("That was no valid input.  Try again...")
			 except ValueError:
			     self.__view.show("Oops!  That was no valid number.  Try again...")
		return {"BMI" : input_data}

	def input_salary(self):
		while True:
			 try:
			     input_data = self.__view.input("Please input the 2or3 digit salary : ")
			     if self.validator.is_valid_salary(input_data):
			     	break
			     else:
			     	self.__view.show("That was no valid input.  Try again...")
			 except ValueError:
			     self.__view.show("Oops!  That was no valid number.  Try again...")
		return {"Salary" : input_data}

	def input_birthday(self):
		while True:
			 try:
			     input_data = self.__view.input("Please input the birthday day-month-year : ")
			     if self.validator.is_valid_birthday(input_data):
			     	break
			     else:
			     	self.__view.show("That was no valid input.  Try again...")
			 except ValueError:
			     self.__view.show("Oops!  That was no valid number.  Try again...")
		return {"Birthday" : input_data}