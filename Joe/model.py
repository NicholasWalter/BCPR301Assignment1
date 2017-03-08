class Model(object):
	"""docstring for Model"""
	#cmd_view = inject.instance(CLI)
	
	def __init__(self):
		self.emploees = []
	def add_the_emploee(self, data):
		print(data)