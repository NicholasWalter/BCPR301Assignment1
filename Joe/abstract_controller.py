from abc import ABCMeta, abstractmethod


class AbstractController(metaclass=ABCMeta):

    @abstractmethod
    def new_employee(self):
        pass

    @abstractmethod
    def load_file(self):
        pass

    def save_file(self):
        pass

    def convert_dict(self):
        pass

    def serialise_objects(self):
        pass

    def display_bar(self):
        pass

    def db_save(self):
        pass
