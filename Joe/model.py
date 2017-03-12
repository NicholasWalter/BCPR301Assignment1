from employee import Employee 

class Model(object):
	"""docstring for Model"""
	#cmd_view = inject.instance(CLI)
	
	def __init__(self):
		self.emploees = []
	def add_the_employee(self, data):
		new_employee = Employee(data['EMPID'],data['Gender'],data['Age'],data['Sales'],data['BMI'],data['Birthday'])
		print(new_employee)