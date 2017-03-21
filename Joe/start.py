'''
    Welcome to Employees Management System.

    Command arguments:

        To input a file :

            python start.py -i <directory path of inputfile>

        To start the program without inputting a file :

            python start.py -s <directory path of inputfile>

        help:

            python start.py -h
'''
import os
import sys
import getopt
sys.path.append(os.getcwd())
from cmd_view import CLI
from controller import Controller
from model import Model
cli = CLI()
model = Model()
ctl = Controller(cli, model)
cli.set_controller(ctl)
try:
    opts, args = getopt.getopt(sys.argv[1:], "hi:s", ["ifile="])
except getopt.GetoptError:
    print('syntax: start.py -i <directory path of inputfile>')
    print('-- inputfile')
    print('syntax: start.py -s')
    print('-- start the system')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print(__doc__)
        sys.exit()
    elif opt in ("-i", "--ifile"):
        inputfile = arg
        cli.do_load(inputfile)
        cli.cmdloop()
    elif opt in ("-s"):
        cli.cmdloop()
