# This file contains the functions which convert the mathematical expression to an easier expression to calculate

import Configuration as Config


def remove_white_spaces(expression: str) -> str:
    """
    Removes all white spaces from the mathematical expression
    :param expression: The mathematical expression
    :return: The mathematical expression without white spaces (\t, \n and spaces)
    """
    removed_white_spaces = ""
    for element in expression:
        if element not in Config.white_spaces:
            removed_white_spaces += element

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


def convert_chars_to_numbers(expression: list) -> list:
    """
    Converts all the chars which contain a number to the true float number.
    If there is more than one decimal point in a number, the custom exception OneDecimalPointException raises.
    If there is a decimal point without a number, the custom exception DecimalPointWithoutNumberException raises
    :param expression: The expression as a list
    :return: The expression which single chars are assembled as numbers
    """
    converted_numbers_expression = list()
    decimal_point_number = 0
    expression_index = 0
    while expression_index < len(expression):
        string_number = ""

        while expression_index < len(expression) and (expression[expression_index].isnumeric() or
                                                      expression[expression_index] == '.'):
            if expression[expression_index] == '.':
                decimal_point_number += 1
                if decimal_point_number > 1:
                    pass

            string_number += expression[expression_index]
            expression_index += 1

        if decimal_point_number > 0:
            pass

        if string_number != "":
            converted_numbers_expression.append(float(string_number))

        if expression_index < len(expression):
            converted_numbers_expression.append(expression[expression_index])
        expression_index += 1

    return converted_numbers_expression


def unary_minus_to_tilda(expression: list) -> list:
    """
    Switches unary minuses to a tilda
    :param expression: The mathematical expression
    :return: The mathematical expression which every unary minus becomes a tilda
    """
    removed_additional_minuses = list()

    for index in range(len(expression)):
        # If a minus comes after another minus or a tilda, it is an unary minus
        if index > 0 and expression[index] == '-' and (expression[index - 1] == '-' or expression[index - 1] == '~' or
                                                       expression[index - 1] == '('):
            removed_additional_minuses.append('~')
        else:
            removed_additional_minuses.append(expression[index])
    return removed_additional_minuses
