"""
this module offers functionality to send messages to the administrator module
currently in use.
once initialized with and administrator module, normal and error messages can be
sent to this module from every other module by importing this.
This makes future expansion with for example a GUI administrator easier as the
new module will only have to implement the stdOut and stdErr messages instead of
retrofitting every other module that needs to pass messages.
"""


IO_target = None

def initialize(target):
    global IO_target
    IO_target = target

def stdOut(message):
    if IO_target:
        IO_target.stdOut(message)

def stdErr(message):
    if IO_target:
        IO_target.stdErr(message)