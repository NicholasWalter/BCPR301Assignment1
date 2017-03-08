import cmd
import string
import sys

#from controller import Controller 

class CLI(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '> '
        #self.input = ''
        #self.ctl = null

    def set_controller(self, ctl):
        self.ctl = ctl

    def do_hello(self, arg):
        print ("hello again", arg, "!")

    def help_hello(self):
        print ("syntax: hello [message]"),
        print ("-- prints a hello message")

    def do_quit(self, arg):
        sys.exit(1)

    def help_quit(self):
        print ("syntax: quit"),
        print ("-- terminates the application")
    # shortcuts
    do_q = do_quit

    def do_new(self, arg):
        self.ctl.new_employee()

    def input(self, arg): 
         input_data = input(arg)

         return input_data
    def show(self, arg = None, arg1 = None):
        if not arg1:
            print (arg)
        else:
            print (arg, arg1)
        
    #def show_two_arguments(self, arg, arg1):
   #     print (arg, arg1)
#
# try it out
