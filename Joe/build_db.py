import sqlite3

try:
    connection = sqlite3.connect("company.db")
except Exception as e:
    print(e)
else:
    print("Opened database successfully")
finally:
    print("Finishing connecting to database")

cursor = connection.cursor()

# delete
try:
	cursor.execute("""DROP TABLE employee;""")
except Exception as e:
    print(e)

sql_command = """
CREATE TABLE employee (
staff_id VARCHAR PRIMARY KEY,
gender CHAR(1),
age VARCHAR(10),
sales VARCHAR(10),
bmi VARCHAR(20),
salary VARCHAR(10),
birthday DATE);"""


try:
	cursor.execute(sql_command)
except Exception as e:
    print(e)

staff_data = [('T123', 'M', '20', '654', 'Normal', '56', '10-18-1996'),
				('T124', 'M', '20', '654', 'Normal', '56', '10-18-1996'),
				('T125', 'M', '20', '654', 'Normal', '56', '10-18-1996'),
				# ('T126', 'M', '20', '654', 'Normal', '56', '10-18-1996'),
				# ('T127', 'M', '20', '654', 'Normal', '56', '10-18-1996'),
				# ('T128', 'M', '20', '654', 'Normal', '56', '10-18-1996'),
				# ('T129', 'M', '20', '654', 'Normal', '56', '10-18-1996'),
				]

for p in staff_data:
	format_str = """INSERT INTO employee (staff_id, gender, age, sales, bmi, salary, birthday)
	VALUES ("{id}", "{gender}", "{age}", "{sales}", "{bmi}", "{salary}", "{birthday}");"""
	sql_command = format_str.format(id=p[0], gender=p[1], age=p[2], sales = p[3], bmi = p[4], salary = p[5], birthday = p[6])
	cursor.execute(sql_command)
connection.commit()

connection.close()

