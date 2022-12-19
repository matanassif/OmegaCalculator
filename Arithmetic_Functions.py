# This file contains all the required arithmetic functions

import Exceptions


def add(first_number: float, second_number: float) -> float:
    """
    Adds the two given numbers
    :param first_number: A number which is used as an operand for addition
    :param second_number: A number which is used as an operand for addition
    :return: The sum of the two given numbers
    """
    return first_number + second_number


def sub(first_number: float, second_number: float) -> float:
    """
    Subtracts the two given numbers
    :param first_number: A number which is used as an operand for subtraction
    :param second_number: A number which is used as an operand for subtraction
    :return: The difference of the two given numbers
    """
    return first_number - second_number


def mul(first_number: float, second_number: float) -> float:
    """
    Multiplies the two given numbers
    :param first_number: A number which is used as an operand for multiplication
    :param second_number: A number which is used as an operand for multiplication
    :return: The result of the multiplication of the two given numbers
    """
    return first_number * second_number


def div(first_number: float, second_number: float) -> float:
    """
    Divides the two given numbers
    :param first_number: A number which is used as an operand for division
    :param second_number: A number which is used as an operand for division
    :return: The result of the division of the two given numbers
    """
    try:
        return first_number / second_number
    except ZeroDivisionError as zde:
        print(str(zde))


def power(first_number: float, second_number: float) -> float:
    """
    Multiplies the first_number, second_number times
    :param first_number: The base of the power
    :param second_number: The exponent of the power
    :return: The result of first_number in the power of second_number
    """
    try:
        if first_number == 0 and second_number == 0:
            raise ValueError("0 to the power of 0 is undefined mathematically")
        result = first_number ** second_number
        if isinstance(result, complex):
            raise Exceptions.ComplexNumberException("The calculator does not support complex numbers")
        return result
    except OverflowError:
        raise ValueError("Result is too big for power")


def modulo(first_number: float, second_number: float) -> float:
    """
    Calculates the remainder of the division of the two given numbers
    :param first_number: The divided number
    :param second_number: The divider number
    :return: The remainder of the division of the two given numbers
    """
    return first_number % second_number


def maximum(first_number: float, second_number: float) -> float:
    """
    Return the bigger number between the two given numbers
    :param first_number: One of the numbers which may be the maximum
    :param second_number: One of the numbers which may be the maximum
    :return: The bigger number between the two given numbers
    """
    if first_number > second_number:
        return first_number
    return second_number


def minimum(first_number: float, second_number: float) -> float:
    """
    Return the smaller number between the two given numbers
    :param first_number: One of the numbers which may be the minimum
    :param second_number: One of the numbers which may be the minimum
    :return: The smaller number between the two given numbers
    """
    if first_number < second_number:
        return first_number
    return second_number


def average(first_number: float, second_number: float) -> float:
    """
    Return the average of the two given numbers
    :param first_number: One of numbers of the average
    :param second_number: One of numbers of the average
    :return: The average of the two given numbers
    """
    return (first_number + second_number) / 2


def negative(number: float) -> float:
    """
    Changes the sign of the number
    :param number: The number which its sign is being changed
    :return: The number with the opposite sign
    """
    return -1 * number


def factorial(number: int) -> int:
    """
    Multiplies the number with all the native numbers before it
    :param number: The number which is being multiplied by all the native numbers before it
    :return: The the multiplication of number with all the native numbers before it
    """
    try:
        if number != int(number) or number < 0:
            raise ValueError("Number in factorial must be positive and not contain a decimal point")
        elif number == 0:
            return 1
        return number * factorial(number - 1)

    # For numbers which are too big
    except RecursionError:
        raise ValueError("Result is too big for factorial")


def add_digits(number: float) -> float:
    """
    Adds the number's digits
    :param number: The number which its digits are being summed
    :return: The sum of the number's digits
    """
    is_signed = False
    if number < 0:
        is_signed = True
        number *= -1

    sum_of_digits = 0
    for letter in str(number):
        if letter != ".":
            sum_of_digits += int(letter)

    if is_signed:
        sum_of_digits *= -1
    return sum_of_digits
