# This file contains the functions which convert the mathematical expression to an easier expression to calculate

import Configuration as Config
import Exceptions


def remove_white_spaces(expression: str) -> str:
    """
    Removes all white spaces from the mathematical expression
    :param expression: The mathematical expression
    :return: The mathematical expression without white spaces (\t, \n and spaces)
    """
    removed_white_spaces = ""

    # Checking if the expression is empty
    if expression == "":
        raise Exceptions.EmptyExpressionException("The expression can not be empty")

    for element in expression:
        if element not in Config.white_spaces:
            removed_white_spaces += element

    # Checking if the expression contains only white spaces
    if removed_white_spaces == "":
        raise Exceptions.OnlyWhiteSpacesException("The expression can not contain only white spaces")

    return removed_white_spaces


def convert_to_list(expression: str) -> list:
    """
    Converts the string expression to a list
    :param expression: The mathematical expression without white spaces
    :return: The expression as a list (each element gets a cell)
    """
    list_expression = list()
    for element in expression:
        list_expression.append(element)

    return list_expression


def convert_chars_to_numbers(expression: str) -> list:
    """
    Converts all the chars which contain a number to the true float number.
    If there is more than one decimal point in a number, the custom exception OneDecimalPointException raises.
    If there is a decimal point without a number, the custom exception DecimalPointWithoutNumberException raises
    :param expression: The expression as a list
    :return: The expression which single chars are assembled as numbers
    """
    converted_numbers_expression = list()
    expression_index = 0
    while expression_index < len(expression):
        string_number = ""
        decimal_point_number = 0

        # Converts chars to a string of a number
        while expression_index < len(expression) and (expression[expression_index].isnumeric() or
                                                      expression[expression_index] == '.'):
            if expression[expression_index] == '.':
                decimal_point_number += 1
                if decimal_point_number > 1:
                    raise Exceptions.OneDecimalPointException(f"The is more than one decimal point "
                                                              f"at index: {expression_index} "
                                                              f"in the expression: {expression}")

            string_number += expression[expression_index]
            expression_index += 1

        # Converts the  string of a number to float
        if string_number != "":
            if string_number == ".":
                raise Exceptions.DecimalPointWithoutNumberException(f"There is a decimal point without a number "
                                                                    f"at index: {expression_index} "
                                                                    f"in the expression: {expression}")
            converted_numbers_expression.append(float(string_number))

        # Adding if expression[expression_index] is not a number
        if expression_index < len(expression):
            converted_numbers_expression.append(expression[expression_index])

        expression_index += 1

    return converted_numbers_expression


def unary_minus_to_tilda(expression: list) -> list:
    """
    Switches unary minuses to a tilda and convert even amount of '-' to '+' and odd amount of '-' to '-'
    according to way number 2
    :param expression: The mathematical expression
    :return: The mathematical expression which every unary minus becomes a tilda
    """
    removed_additional_minuses = list()
    expression_index = 0
    while expression_index < len(expression):
        # If a minus comes after another minus or a tilda, it is an unary minus
        if expression[expression_index] == '-':

            # The minus is not unary and should be converted to '-' or '+' depending on the amount of minuses
            if expression_index > 0 and (type(expression[expression_index-1]) == float
                                         or expression[expression_index-1] == '+'
                                         or Config.position[expression[expression_index-1]] == "right"
                                         or expression[expression_index-1] == ")"):
                # Counts the minuses
                minus_counter = 0
                first_in_a_row_minus_index = expression[expression_index-1]
                while expression_index < len(expression) and expression[expression_index] == '-':
                    minus_counter += 1
                    expression_index += 1

                # Inserts one minus if the count is odd, otherwise inserts a '+' unless there is already a '+' before
                expression_index -= 1
                if minus_counter % 2 != 0:
                    if first_in_a_row_minus_index == '+':
                        removed_additional_minuses.pop(-1)
                    removed_additional_minuses.append('-')
                elif first_in_a_row_minus_index != '+':
                    removed_additional_minuses.append('+')

            # The minus is unary
            else:
                removed_additional_minuses.append('~')

        else:
            removed_additional_minuses.append(expression[expression_index])

        expression_index += 1

    return removed_additional_minuses


def shorten_tilda(expression: list) -> list:
    """
    Shorten a sequence of tildas to one or zero
    :param expression: The mathematical expression which every unary minus becomes a tilda
    :return: The mathematical expression which the sequences of tildas are shorten to one or zero
    """
    # The expression without sequences of tildas after conversion of minuses to tildas
    no_tilda_sequences = list()
    expression_index = 0

    while expression_index < len(expression):
        if expression[expression_index] == '~':
            tilda_counter = 0

            # Counts the tildas
            while expression_index < len(expression) and expression[expression_index] == '~':
                tilda_counter += 1
                expression_index += 1

            # Inserts one tilda if the count is odd, otherwise does not insert anything
            expression_index -= 1
            if tilda_counter % 2 != 0:
                no_tilda_sequences.append('~')

        # Adds every element which is not a tilda
        else:
            no_tilda_sequences.append(expression[expression_index])

        expression_index += 1

    return no_tilda_sequences
