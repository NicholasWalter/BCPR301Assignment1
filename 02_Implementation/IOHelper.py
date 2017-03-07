IO_target = None

def initialize(new_IO_target):
    global IO_target
    print("initializing IO helper")
    IO_target = new_IO_target

def stdOut(message):
    if IO_target:
        IO_target.stdOut(message)

def stdErr(message):
    if IO_target:
        IO_target.stdErr(message)