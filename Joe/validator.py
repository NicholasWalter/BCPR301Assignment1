class Validator(object):
	"""docstring for ClassName"""
	#def __init__(self):
	def is_valid_employee_id(self, input_data):
		result = False
		if input_data.__len__() > 0:
			num_ascii = ord(input_data[0])
			if num_ascii > 64 and num_ascii < 91:
				int_digit = input_data[1::]
				print(int_digit)
				if int_digit.isdigit() and int_digit.__len__() == 3:
					result = True
				else:
					result = False
			else:
				result = False
			#print(result)
		return result
	def is_valid_gender(self, input_data):
		result = False
		if input_data == 'M' or input_data == 'F':
			result = True
		else:
			result = False
		return result
	def is_valid_age(self, input_data):
		result = False
		if input_data.isdigit() and input_data.__len__() == 2:
			result = True
		else:
			result = False
		return result
	def is_valid_sales(self, input_data):
		result = False
		if input_data.isdigit() and input_data.__len__() == 3:
			result = True
		else:
			result = False
		return result
	def is_valid_BMI(self, input_data):
		result = False
		options = ['Normal', 'Overweight', 'Obesity', 'Underweight']
		if input_data in options:
			result = True
		else:
			result = False
		return result
	def is_valid_salary(self, input_data):
		result = False
		if input_data.isdigit() and input_data.__len__() >= 2 and input_data.__len__() <= 3:
			result = True
		else:
			result = False
		return result
# if __name__ == '__main__':
# 	v = Validator()
# 	data = input("input ID :")
# 	v . is_valid_employee_id(data) 