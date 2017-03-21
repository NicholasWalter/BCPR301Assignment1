'''
 Hello this is the xxxxxxdsadasd
'''
import cmd
import string
import sys

#from controller import Controller


class CLI(cmd.Cmd):

    '''
     Hello this is the xxxxxxdsadasd
    '''

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '> '
        self.show(__doc__)

    def set_controller(self, ctl):
        self.ctl = ctl

    def do_quit(self, arg):
        '''
        syntax: quit
        -- terminates the application
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
        -- add an employee    
        '''
        self.ctl.new_employee()

    def do_load(self, path):
        self.ctl.load_file(path)

    def help_load(self):
        print("syntax: load [path of the file]"),
        print("-- add the file data")

    def do_save(self, path):
        self.ctl.save_file(path)

    def help_save(self):
        print("syntax: save [path of the file]"),
        print("-- save data in local storage")

    def do_serialise(self, path):
        self.ctl.serialise_objects(path)

    def help_serialise(self):
        print("syntax: serialise [path of the file]"),
        print("-- add the file data")

    def do_line_chart(self, arg):
        self.ctl.display_bar()

    def help_line_chart(self):
        print("syntax: line_chart")
        print("-- display a line_chart in chrome")

    def do_db_save(self, arg):
        self.ctl.db_save()

    def help_db_save(self):
        print("syntax: db_save")
        print("-- save date in database")

    def do_db_load(self, arg):
        self.ctl.db_load()


    def help_db_load(self):
        print("syntax: db_load")
        print("-- load data from database")

    def input(self, arg):
        input_data = input(arg)

        return input_data

    def show(self, arg=None, arg1=None):
        if not arg1:
            print(arg)
        else:
            print(arg, arg1)

    def do_test(self, arg):
        self.ctl.test(arg)
    # def show_two_arguments(self, arg, arg1):
   #     print (arg, arg1)
#
# try it out
