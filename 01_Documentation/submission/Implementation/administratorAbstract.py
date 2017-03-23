"""
this module offers the AdministratorAbstract class

since this module only offers an interface for other classes to implement and
no actual functionality, nothing can be tested in here.
"""

# python imports
from abc import abstractmethod, ABCMeta

class AdministratorAbstract(metaclass=ABCMeta):
    """
    this is an abstract class to define the interface of all Administrator
    classes.
    """

    def __init__(self):
        super().__init__()
        pass

    @abstractmethod
    def stdOut(self):
        pass

    @abstractmethod
    def stdErr(self):
        pass