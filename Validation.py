# This file contains functions which check if the given input is valid or not

import Configuration as Config
import Convertion as Convert


def check_legal_elements(expression: str):
    """
    Checks if all the elements in the given expression are legal elements
    :param expression: The given mathematical expression without white spaces
    :return: Raises an exception if there are illegal elements in the given expression
    """
    for element in expression:
        if element not in Config.legal_elements:
            raise...


def amount_of_bracket(expression: str):
    """
    Checks if the amount of opening bracket is equal to the amount of closing brackets
    :param expression: The given mathematical expression without white spaces
    :return: Raises an exception if the amount of opening bracket is not equal to the amount of closing brackets
    """
    opening_bracket_amount = 0
    closing_bracket_amount = 0
    for element in expression:
        if element == '(':
            opening_bracket_amount += 1
        elif element == ')':
            closing_bracket_amount += 1

    if opening_bracket_amount != closing_bracket_amount:
        raise...


def check_tilda(expression: list):
    """
    Checks if after a tilda there is another tilda before a number comes
    :param expression: The mathematical expression in list form
    :return: Raises an exception if after a tilda there is another tilda before a number comes
    """
    # If tilda flag is True, then there was a tilda and after it there was no number or opening bracket yet
    tilda_flag = False

    for element in expression:
        if element == '~':
            if tilda_flag:
                raise...
            else:
                tilda_flag = True
        elif type(element) == float or element == '(':
            tilda_flag = False


def operator_operand_order_right(current: str, previous_element, next_element):
    """
    Checks if the validation of the positioning of a right positioned operator
    :param current: The current element in the expression
    :param previous_element: The previous element in the expression
    :param next_element: The next element in the expression
    :return: Raises an error if needed
    """
    # Can not be first element
    if previous_element is None:
        raise...

    # The element before it must be a number and after it only a "mid" positioned operator or a closing bracket
    elif type(previous_element) != float:

        # If the operator can appear more than once in a row, the previous element may be the same operator
        if current in Config.in_a_row_operators:
            if previous_element != current:
                raise...
        else:
            raise...

    elif not(Config.position[next_element] == "mid" or next_element == ')'):

        # If the operator can appear more than once in a row, the next element may be the same operator
        if current in Config.in_a_row_operators:
            if next_element != current:
                raise ...
        else:
            raise ...


def operator_operand_order_left(current: str, previous_element, next_element):
    """
    Checks if the validation of the positioning of a left positioned operator
    :param current: The current element in the expression
    :param previous_element: The previous element in the expression
    :param next_element: The next element in the expression
    :return: Raises an error if needed
    """
    # Can not be last element
    if next_element is None:
        raise...

    # The element after it must be a number and after it only a "mid" positioned operator or a closing bracket
    elif type(next_element) != float:

        # If the operator can appear more than once in a row, the next element may be the same operator
        if current in Config.in_a_row_operators:
            if next_element != current:
                raise ...
        else:
            raise ...

    elif not (Config.position[previous_element] == "mid" or previous_element == '('):

        # If the operator can appear more than once in a row, the previous element may be the same operator
        if current in Config.in_a_row_operators:
            if previous_element != current:
                raise ...
        else:
            raise ...


def operator_operand_order_mid(current: str, previous_element, next_element):
    """
    Checks if the validation of the positioning of a mid positioned operator
    :param current: The current element in the expression
    :param previous_element: The previous element in the expression
    :param next_element: The next element in the expression
    :return: Raises an error if needed
    """
    if next_element is None or (previous_element is None and previous_element in Config.beginning_operators):
        raise...

    # The element after it must be a number and after it only a "mid" positioned operator or a closing bracket
    elif type(previous_element) != float:
        if previous_element in Config.operators and (Config.position[previous_element] != "right" or previous_element != ')'):

            # If the operator can appear more than once in a row, the next element may be the same operator
            if current in Config.in_a_row_operators:
                if previous_element != current:
                    raise ...
            else:
                raise ...

    elif type(next_element) != float:

        # If the operator can appear more than once in a row, the previous element may be the same operator
        if next_element in Config.operators and (Config.position[next_element] != "left" or next_element != '('):

            # If the operator can appear more than once in a row, the next element may be the same operator
            if current in Config.in_a_row_operators:
                if next_element != current:
                    raise ...
            else:
                raise ...


def operator_operand_order_brackets(current: str, previous_element, next_element):
    """
    Checks if the validation of the positioning of a bracket
    :param current: The current element in the expression
    :param previous_element: The previous element in the expression
    :param next_element: The next element in the expression
    :return: Raises an error if needed
    """
    if current == '(':
        if next_element is None:
            raise ...
        elif type(previous_element) == float or Config.position[previous_element] == "left" or previous_element == ')':
            raise ...
        elif Config.position[next_element] == "left" or next_element == ')' or next_element not in Config.beginning_operators:
            raise ...

    elif current == ')':
        if previous_element is None:
            raise ...
        elif Config.position[previous_element] == "right" or previous_element == '(' or previous_element not in Config.end_operators:
            raise ...
        elif type(next_element) == float or Config.position[next_element] == "right" or next_element == '(':
            raise ...


def check_number(previous_element, next_element):
    """
    Checks if the validation of the positioning of a number
    :param previous_element: The previous element in the expression
    :param next_element: The next element in the expression
    :return: Raises an error if needed
    """
    if not(previous_element is None) and (Config.position[previous_element] == "right" or Config.position[previous_element] == ')'):
        raise ...
    if not(next_element is None) and (Config.position[next_element] == "left" or Config.position[next_element] == '('):
        raise ...


def operator_operand_order(expression: list):
    """
    Checks if operator-operand order is legal
    :param expression: The mathematical expression in list form with after conversion of unary minus to tilda
    :return: Raises an exception if operator-operand order is illegal
    """
    for index in range(len(expression)):
        current = expression[index]

        if index == 0:
            previous_element = None
            next_element = expression[index + 1]
        elif index == len(expression) - 1:
            next_element = None
            previous_element = expression[index - 1]
        else:
            previous_element = expression[index - 1]
            next_element = expression[index + 1]

        # Number can be the first or last element
        if type(current) == float:
            check_number(previous_element, next_element)

        elif current != '(' and current != ')':
            if Config.position[current] == "mid":
                operator_operand_order_mid(current, previous_element, next_element)
            elif Config.position[current] == "right":
                operator_operand_order_right(current, previous_element, next_element)
            else:
                operator_operand_order_left(current, previous_element, next_element)

        else:
            operator_operand_order_brackets(current, previous_element, next_element)


def validate_and_convert(expression: str) -> list:
    """
    Checks validation and converts the mathematical expression to an easier expression to calculate
    :param expression: The given mathematical expression
    :return: Raises an exception if there are illegal elements in the given expression
    """
    # Removes all white spaces from the mathematical expression
    infix_expression = Convert.remove_white_spaces(expression)

    # Checks if all the elements in the given expression are legal elements
    check_legal_elements(infix_expression)

    # Checks if the amount of opening bracket is equal to the amount of closing brackets
    amount_of_bracket(infix_expression)

    # Converts the string expression to a list
    infix_expression_list = Convert.convert_to_list(infix_expression)

    # Checks if after a tilda there is another tilda before a number comes
    check_tilda(infix_expression_list)

    # Converts all the chars which contain a number to the true float number.
    infix_expression_list = Convert.convert_chars_to_numbers(infix_expression_list)

    # Checks if operator-operand order is legal
    operator_operand_order(infix_expression_list)

    # Switches unary minuses to a tilda and convert even amount of '-' to '+' according to way number 2
    infix_expression_list = Convert.unary_minus_to_tilda(infix_expression_list)
    return infix_expression_list
