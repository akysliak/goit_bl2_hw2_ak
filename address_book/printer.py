from addressbook import *
from abc import ABC, abstractmethod
import warnings


class CLIPrinter(ABC):

    @abstractmethod
    def print_to_cl(self, *args):
        pass


class SimpleMessagePrinter(CLIPrinter):
    """
    Prints simple messages in the command line.
    """

    @staticmethod
    def print_to_cl(message: str):
        print(message)


class ExceptionPrinter(CLIPrinter):
    """
    Prints exceptions to the command line
    """
    EXCEPTION_COLOR = '\033[91m'  # '\033[92m' #'\033[93m'
    RESET_COLOR = '\033[0m'

    @staticmethod
    def print_to_cl(exception: MyException):
        print(str(exception).replace('"', ""))
        #message = str(exception).replace('"', "")
        #print(f"{ExceptionPrinter.EXCEPTION_COLOR}{message}{ExceptionPrinter.RESET_COLOR}")


class WarningPrinter(CLIPrinter):
    """
    Prints warnings to the command line.
    """
    WARNING_COLOR = '\033[93m'  # '\033[92m' #'\033[93m'
    RESET_COLOR = '\033[0m'

    @staticmethod
    def print_to_cl(warning: Exception):
        print(f"{WarningPrinter.WARNING_COLOR}{warning.message}{WarningPrinter.RESET_COLOR}")


class InputRequest(CLIPrinter):
    """
    Requests an input from the user.
    """
    @staticmethod
    def print_to_cl(message: str = "AddressBook:"):
        return input(f"{message} ")