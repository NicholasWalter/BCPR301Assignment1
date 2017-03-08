"""
this module offers the DataHandlerDataBase class, opening connections to a
MySQL database to save and read employees to and from.
"""

# python imports
import pymysql

# project imports
from dataHandlerAbstract import DataHandlerAbstract

class DataHandlerDataBase(DataHandlerAbstract):
    
    def __init__(self, db_ip, db_username, db_password, db):
        self.db_ip = db_ip
        self.db_username = db_username
        self.db_password = db_password
        self.db = db

    def _execute_command(command)
        db = pymysql.connect(self.db_ip, self.db_username, self.db_password,
                                self.db)
        output = []
        cursor = db.cursor()
        cursor.execute(command)

        line = cursor.fetchone()
        while line is not None:
            output.append(line)
            line = cursor.fetchone()

        db.close()
        return output