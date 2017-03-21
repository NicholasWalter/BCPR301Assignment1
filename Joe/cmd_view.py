'''
     Welcome to Employee Management System terminal !!!

     Command :
        syntax: add
        -- start an asking process to add an employee

        syntax: load [path of the TXT file]
        -- load the data from the file

        syntax: save [path of the file]
        -- save data as txt file in local storag

        syntax: serialise [path of the file]
        -- save object in data.pickle file at local storage

        syntax: line_chart
        -- display a line_chart in chrome

        syntax: db_save
        -- save date in database
    
        syntax: db_load
        -- load data from database

        syntax: show_all
        -- display all the data in the system

        syntax: quit
        -- quit the program
'''
import cmd
import string
import sys

#from controller import Controller


class CLI(cmd.Cmd):

    '''


    '''

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '> '
        # self.show(__doc__)

    def set_controller(self, ctl):
        self.ctl = ctl

    def do_quit(self, arg):
        '''
        syntax: quit
        -- terminates the application
        parameters: -
        output: -
        '''
        sys.exit(1)

    # def help_quit(self):
    #     print("syntax: quit"),
    #     print("-- terminates the application")
    # shortcuts
    # do_q = do_quit

    def do_add(self, arg):
        '''
        syntax: add
        -- start an asking process to add an employee
        parameters:
            e.g.    id : D123
                gender : M
                   age : 23
                 sales : 456
                   BMI : Normal
                salary : 54
              brithday : 12-1-1991
        output : data string and keyword : success 
        '''
        self.ctl.new_employee()

    def do_load(self, path):
        '''
        syntax: load [path of the TXT file]
        -- load the data from the file
        parameters:
            the path of the TXT file
        output:
            "success" | "invalid data" | "error : wrong path"

        '''
        self.ctl.load_file(path)

    # def help_load(self):
    #     print("syntax: load [path of the file]"),
    #     print("-- add the file data")

    def do_save(self, path):
        '''
        syntax: save [path of the file]
        -- save data as txt file in local storag
        parameters:
            path of the local storage
        output:
            TXT file and "ok" 
                    or
            "error : wrong path"
                "not data"
        '''
        self.ctl.save_file(path)

    # def help_save(self):
    #     print("syntax: save [path of the file]"),
    #     print("-- save data in local storage")

    def do_serialise(self, path):
        '''
        syntax: serialise [path of the file]
        -- save object in data.pickle file at local storage
        parameters:
            path of the local storage
        output:
            data.pickle file and "ok" 
                    or
            "error : wrong path"
               "data error"
        '''
        self.ctl.serialise_objects(path)

    # def help_serialise(self):
    #     print("syntax: serialise [path of the file]"),
    #     print("-- add the file data")

    def do_line_chart(self, arg):
        '''
        syntax: line_chart
        -- display a line_chart in chrome
        parameters:--
        output:
            display a line chart in chrome
                     or
                "data error"
        '''
        self.ctl.display_bar()

    # def help_line_chart(self):
    #     print("syntax: line_chart")
    #     print("-- display a line_chart in chrome")

    def do_db_save(self, arg):
        '''
        syntax: db_save
        -- save date in database
        parameters:--
        output:
            a list of data and keyword "ok"             
                        or
                "no data to save"
        '''
        self.ctl.db_save()

    def do_show_all(self, arg):
        '''
        syntax: show_all
        -- display all the data in the system
        parameters:--
        output:
                a list of data            
                    or
                "not data"
        '''
        self.ctl.print_all_data()
    # def help_db_save(self):
    #     print("syntax: db_save")
    #     print("-- save date in database")

    def do_db_load(self, arg):
        '''
        syntax: db_load
        -- load data from database
        parameters:--
        output:
            a list of data
                 or
            "no data"
        '''
        self.ctl.db_load()

    # def help_db_load(self):
    #     print("syntax: db_load")
    #     print("-- load data from database")

    def input(self, arg):
        input_data = input(arg)
        return input_data

    def show(self, arg=None, arg1=None):
        if not arg1:
            print(arg)
        else:
            print(arg, arg1)

    # def show_two_arguments(self, arg, arg1):
   #     print (arg, arg1)
#
# try it out
