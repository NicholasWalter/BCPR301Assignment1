import sqlite3
import time


class DB(object):
	def __init__(self, name):
		self.db_name = name
		self.db_connection = None
		self.db_cursor = None

	def db_connect(self):
		try:
		    self.db_connection = sqlite3.connect(self.db_name)
		    self.db_cursor = self.db_connection.cursor()
		except Exception as e:
		    print(e)
		else:
		    print("Opened database successfully")

		finally:
		    print("Finishing connecting to database")

    # def query(query):
    # 	self.db_cursor.execute(query)
	def close(self):
		self.db_connection.close()

	def commit(self):
		try:
			self.db_connection.commit()
		except Exception as e:
		    print(e)

	def insert_employee_data(self, list):
		try:
			self.db_connect()
			for p in list:
				format_str = """INSERT INTO employee (staff_id, gender, age, sales, bmi, salary, birthday) VALUES ("{id}", "{gender}", "{age}", "{sales}", "{bmi}", "{salary}", "{birthday}");"""
				sql_command = format_str.format(id=p[0], gender=p[1], age=p[2], sales=p[3], bmi=p[4], salary=p[5], birthday=p[6])
				try:
					self.db_cursor.execute(sql_command)
				except Exception as e:
					print(e)
				time.sleep(0.25)
		except Exception as e:
			print(e)
		finally:
			self.commit()
			self.close()

	def fetch_all_employees(self):
		try:
			self.db_connect()
			self.db_cursor.execute("SELECT * FROM employee")
			print("fetchall:")
			result = self.db_cursor.fetchall()
			for r in result:
				print(r)
			return result
		except Exception as e:
			print(e)
		finally:
			self.close()


staff_data = [('T123', 'M', '20', '654', 'Normal', '56', '10-18-1996'),
				('T124', 'M', '20', '654', 'Normal', '56', '10-18-1996'),
				('T125', 'M', '20', '654', 'Normal', '56', '10-18-1996'),
				('T126', 'M', '20', '654', 'Normal', '56', '10-18-1996'),
				('T127', 'M', '20', '654', 'Normal', '56', '10-18-1996'),
				('T128', 'M', '20', '654', 'Normal', '56', '10-18-1996'),
				('T129', 'M', '20', '654', 'Normal', '56', '10-18-1996'),
				]

db = DB("company.db")
# db.db_connect()
db.insert_employee_data(staff_data)
# db.commit()
db.fetch_all_employees()