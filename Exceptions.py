# The file contains all the custom exceptions

class ComplexNumberException(Exception):
    """
    The exception is raised when the calculation contains a complex number
    """
    def __init__(self, message):
        super().__init__(message)


class FactorialException(Exception):
    """
    The exception is raised when the number is float or negative
    """
    def __init__(self, message):
        super().__init__(message)


class IllegalElementException(Exception):
    """
    The exception is raised when the expression contains illegal elements
    """
    def __init__(self, message):
        super().__init__(message)


class AmountOfBracketsException(Exception):
    """
    The exception is raised when the amount of opening brackets is not equal to the amount of closing brackets
    """
    def __init__(self, message):
        super().__init__(message)


class TildaInARowException(Exception):
    """
    The exception is raised when there are more than one tilda in a row
    """
    def __init__(self, message):
        super().__init__(message)


class OneDecimalPointException(Exception):
    """
    The exception is raised when there is more than one decimal point in a number
    """
    def __init__(self, message):
        super().__init__(message)


class DecimalPointWithoutNumberException(Exception):
    """
    The exception is raised when there is a decimal point without a number
    """
    def __init__(self, message):
        super().__init__(message)


class FirstElementException(Exception):
    """
    The exception is raised when the first element can not be placed in the beginning of the expression
    """
    def __init__(self, message):
        super().__init__(message)


class LastElementException(Exception):
    """
    The exception is raised when the first element can not be placed in the end of the expression
    """
    def __init__(self, message):
        super().__init__(message)


class PreviousElementException(Exception):
    """
    The exception is raised when the previous element can not be placed in its position
    """
    def __init__(self, message):
        super().__init__(message)


class NextElementException(Exception):
    """
    The exception is raised when the next element can not be placed in its position
    """
    def __init__(self, message):
        super().__init__(message)
