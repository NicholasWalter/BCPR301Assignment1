import datetime
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
	def is_valid_birthday(self, input_data):
		result = False
		#try:
		if(datetime.datetime.strptime(input_data, '%d-%m-%Y')):
			result = True
		else:
			result = False
		#except ValueError: 
		return result
        	#raise ValueError("Incorrect data format, should be YYYY-MM-DD")
	# def is_valid_birthday(self, input_data):
	# 	result = False
	# 	date = input_data.split("-")
	# 	print(date)
	# 	if date.__len__() == 3:
	# 		if date[0].isdigit() and date[0] <= 2:
	# 			if date[1].isdigit() and date[1] <= 2:
	# 				if date[3].isdigit() and date[3] == 4:
	# 					result = True
	# 				else:
	# 					result = False
	# 			else:
	# 				result = False
	# 		else:
	# 			result = False
	# 	else:
	# 		result = False
	# 	return result

# if __name__ == '__main__':
# 	v = Validator()
# 	data = input("input ID :")
# 	v . is_valid_employee_id(data) 