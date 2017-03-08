import os
import sys
sys.path.append(os.getcwd())
from cmd_view import CLI 
from controller import Controller 
from model import Model

cli = CLI()
model = Model()
ctl = Controller(cli, model)
cli.set_controller(ctl)

cli.cmdloop()