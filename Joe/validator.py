import datetime


class Validator(object):

    """docstring for ClassName"""
    # def __init__(self):

    def is_valid_employee_id(self, input_data):
        result = False
        if input_data.__len__() > 0:
            num_ascii = ord(input_data[0])
            if num_ascii > 64 and num_ascii < 91:
                int_digit = input_data[1::]
                #print(int_digit)
                #print(int_digit.__len__())
                if int_digit.isdigit() and int_digit.__len__() == 3:
                    result = True
                else:
                    result = False
            else:
                result = False
        #print(input_data)
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
        try:
            if(datetime.datetime.strptime(input_data, '%d-%m-%Y')):
                date = datetime.datetime.strptime(input_data, '%d-%m-%Y')
                if(date.year > datetime.datetime.now().year):
                    result = False
                else:
                    result = True
            else:
                result = False
            return result
        except ValueError:
            return False

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
    def is_load_data(self, input_data):
        result = 0
        data = input_data.split(',')
        if(data.__len__() == 7):
            if(self.is_valid_employee_id(data[0])):
                result += 1
            if(self.is_valid_gender(data[1])):
                result += 1
            if(self.is_valid_age(data[2])):
                result += 1
            if(self.is_valid_sales(data[3])):
                result += 1
            if(self.is_valid_BMI(data[4])):
                result += 1
            if(self.is_valid_salary(data[5])):
                result += 1
            if(self.is_valid_birthday(data[6])):
                result += 1
        if(result == 7):
            return True
        else:
            return False
