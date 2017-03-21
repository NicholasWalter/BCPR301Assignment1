import pickle


class Serialization(object):

    """ docstring for Controller"""

    def __init__(self):
        self.__pickle = pickle

    def open(self, path, arg):
        return open(path, arg)

    def dump(self, file, obejct):
        self.__pickle.dump(obejct, file)

    def load(self, file):
        return self.__pickle.load(file)

    def close(self, file):
        file.close()
