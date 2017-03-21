from abc import ABCMeta, abstractmethod


class AbstractView(metaclass=ABCMeta):

    @abstractmethod
    def show(self):
        pass

    def input(self):
        pass
