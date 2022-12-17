# This file contains functions which check if the given input is valid or not

import Configuration as Config
import Convertion as Convert
import Exceptions


def check_legal_elements(expression: str):
    """
    Checks if all the elements in the given expression are legal elements
    :param expression: The given mathematical expression without white spaces
    :return: Raises an exception if there are illegal elements in the given expression
    """
    for element in expression:
        if element not in Config.legal_elements:
            raise Exceptions.IllegalElementException(f"The element: {element} is illegal")


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


def check_tilda(expression: str):
    """
    Checks if after a tilda there is another tilda before a number comes
    :param expression: The mathematical expression in list form
    :return: Raises an exception if after a tilda there is another tilda before a number comes
    """
    # If tilda flag is True, then there was a tilda and after it there was no number or opening bracket yet
    tilda_flag = False

    for element_index in range(len(expression)):
        if expression[element_index] == '~':
            if tilda_flag:
                raise Exceptions.TildaInARowException(f"There is more than one tilda in a row in index:{element_index}")
            else:
                tilda_flag = True

        # The expression is still legal
        elif type(expression[element_index]) == float or expression[element_index] == '(':
            tilda_flag = False


def validation_previous_right(current: str, previous_element):
    """
    Checks validation of the previous element of the right positioned operator
    considering the possibility it can appear more than once in a row
    :param current: The current operator in the expression
    :param previous_element: The next element in the expression
    :return: Raises an exception if the operator's place is illegal
    """
    # If the operator can appear more than once in a row, the previous element may be the same operator
    message = f"The element {current} should be after a number"
    if current in Config.in_a_row_operators:
        if previous_element == current:
            return

        message += " or itself"

    raise Exceptions.PreviousElementException(message)


def validation_next_right(current: str, next_element):
    """
    Checks validation of the next element of the right positioned operator
    considering the possibility it can appear more than once in a row
    :param current: The current operator in the expression
    :param next_element: The next element in the expression
    :return: Raises an exception if the operator's place is illegal
    """
    # If the operator can appear more than once in a row, the next element may be the same operator
    message = f"The element {current} should be followed by a mid positioned operator or a '('"
    if current in Config.in_a_row_operators:
        if next_element == current:
            return

        message += " or itself"

    raise Exceptions.NextElementException(message)


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
        raise Exceptions.FirstElementException(f"The element {current} can not be placed in the beginning")

    # Before the element must be a number or a mid positioned operator or a closing bracket
    elif type(previous_element) != float:
        validation_previous_right(current, previous_element)

    # After the element must be a number or a mid positioned operator or an opening bracket
    elif next_element is not None and type(next_element) != float and Config.position[next_element] != "mid" \
            and next_element != ')':
        validation_next_right(current, next_element)


def validation_previous_left(current: str, previous_element):
    """
    Checks validation of the previous element of the left positioned operator
    considering the possibility it can appear more than once in a row
    :param current: The current operator in the expression
    :param previous_element: The next element in the expression
    :return: Raises an exception if the operator's place is illegal
    """
    # If the operator can appear more than once in a row, the previous element may be the same operator
    message = f"The element {current} should be after a mid positioned operator or a '('"
    if current in Config.in_a_row_operators:
        if previous_element == current:
            return

        message += " or itself"

    raise Exceptions.PreviousElementException(message)


def validation_next_left(current: str, next_element):
    """
    Checks validation of the next element of the left positioned operator
    considering the possibility it can appear more than once in a row
    :param current: The current operator in the expression
    :param next_element: The next element in the expression
    :return: Raises an exception if the operator's place is illegal
    """
    # If the operator can appear more than once in a row, the next element may be the same operator
    message = f"The element {current} should be followed by a number"
    if current in Config.in_a_row_operators:
        if next_element == current:
            return

        message += " or itself"

    raise Exceptions.NextElementException(message)


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
        raise Exceptions.LastElementException(f"The element {current} can not be placed in the end")

    # Before the operator must be a number or a mid positioned operator or an opening bracket
    elif previous_element is not None and type(next_element) != float and previous_element != '(' and \
            Config.position[previous_element] != "mid":
        validation_previous_left(current, previous_element)

    # After the operator must be a number or a mid positioned operator or a closing bracket
    elif type(next_element) != float:
        validation_next_left(current, next_element)


def validation_previous_mid(current: str, previous_element):
    """
    Checks validation of the previous element of the mid positioned operator
    considering the possibility it can appear more than once in a row
    :param current: The current operator in the expression
    :param previous_element: The next element in the expression
    :return: Raises an exception if the operator's place is illegal
    """
    # If the operator can appear more than once in a row, the previous element may be the same operator
    message = f"The element {current} should be after a right positioned operator or a ')' or a number"
    if current in Config.in_a_row_operators:
        if previous_element == current:
            return

        message += " or itself"

    raise Exceptions.PreviousElementException(message)


def validation_next_mid(current: str, next_element):
    """
    Checks validation of the next element of the mid positioned operator
    considering the possibility it can appear more than once in a row
    :param current: The current operator in the expression
    :param next_element: The next element in the expression
    :return: Raises an exception if the operator's place is illegal
    """
    # If the operator can appear more than once in a row, the next element may be the same operator
    message = f"The element {current} should be followed by a left positioned operator or a '(' or a number"
    if current in Config.in_a_row_operators:
        if next_element == current:
            return

        message += " or itself"

    raise Exceptions.NextElementException(message)


def operator_operand_order_mid(current: str, previous_element, next_element):
    """
    Checks if the validation of the positioning of a mid positioned operator
    :param current: The current element in the expression
    :param previous_element: The previous element in the expression
    :param next_element: The next element in the expression
    :return: Raises an error if needed
    """
    # Checks validation if the element is the first or last
    if next_element is None or (previous_element is None and previous_element in Config.beginning_operators):
        raise Exceptions.FirstElementException(f"The element {current} can not be placed in the beginning or the end")

    # Before the operator must be a number or a right positioned operator or a closing bracket
    elif previous_element is not None and type(previous_element) != float \
            and Config.position[previous_element] != "right" and previous_element != ')':
        validation_previous_mid(current, previous_element)

    # After the operator must be a number or a left positioned operator or an opening bracket
    elif type(next_element) != float and Config.position[next_element] != "left" and next_element != '(':
        validation_next_mid(current, next_element)


def check_opening_bracket(current: str, previous_element, next_element):
    """
    Checks if the validation of the positioning of an opening bracket
    :param current: The current element in the expression
    :param previous_element: The previous element in the expression
    :param next_element: The next element in the expression
    :return: Raises an error if needed
    """
    # The previous element can be only a number or a right positioned operator or a mid positioned operator
    if previous_element is not None and Config.position[previous_element] != "right" \
            and Config.position[previous_element] != "mid":

        raise Exceptions.PreviousElementException(f"The element {current} should be followed by "
                                                  f"after a left positioned operator or a number")

    # The next element can be only a number or a left positioned operator or a beginning operator
    elif type(next_element) != float and Config.position[next_element] != "left" \
            and next_element not in Config.beginning_operators:

        raise Exceptions.NextElementException(f"The element {current} should be followed by "
                                              f"a left positioned operator or a number")


def check_closing_bracket(current: str, previous_element, next_element):
    """
    Checks if the validation of the positioning of a closing bracket
    :param current: The current element in the expression
    :param previous_element: The previous element in the expression
    :param next_element: The next element in the expression
    :return: Raises an error if needed
    """
    # The previous element can be only a number or a left positioned operator or an end operator
    if previous_element is not None and type(previous_element) != float and \
            Config.position[previous_element] != "right" and previous_element not in Config.end_operators:

        raise Exceptions.PreviousElementException(f"The element {current} should be "
                                                  f"after a right positioned operator or a number")

    # The next element can be only a number or a left positioned operator or a mid positioned operator
    elif next_element is not None and Config.position[next_element] != "right" \
            and Config.position[next_element] != "mid":

        raise Exceptions.NextElementException(f"The element {current} should be followed by "
                                              f"a right positioned operator or a number")


def operator_operand_order_brackets(current: str, previous_element, next_element):
    """
    Checks if the validation of the positioning of a bracket
    :param current: The current element in the expression
    :param previous_element: The previous element in the expression
    :param next_element: The next element in the expression
    :return: Raises an error if needed
    """
    if current == '(':
        # Can not appear last in expression
        if next_element is None:
            raise Exceptions.LastElementException(f"The element {current} can not be placed in the end")

        check_opening_bracket(current, previous_element, next_element)

    elif current == ')':
        # Can not appear first in expression
        if previous_element is None:
            raise Exceptions.FirstElementException(f"The element {current} can not be placed in the beginning")

        check_closing_bracket(current, previous_element, next_element)


def check_number(current: str, previous_element, next_element):
    """
    Checks if the validation of the positioning of a number
    :param current: The current element in the expression
    :param previous_element: The previous element in the expression
    :param next_element: The next element in the expression
    :return: Raises an error if needed
    """
    # Before a number can not be a right positioned element or a closing bracket
    if previous_element is not None and (Config.position[previous_element] == "right" or previous_element == ')'):
        raise Exceptions.PreviousElementException(f"The element {current} should be "
                                                  f"after a left or mid positioned operator or a '('")

    # After a number can not be a left positioned element or an opening bracket
    if next_element is not None and (Config.position[next_element] == "left" or next_element == '('):
        raise Exceptions.NextElementException(f"The element {current} should be followed by "
                                              f"a right or mid positioned operator or a ')'")


def operator_operand_order(expression: list):
    """
    Checks if operator-operand order is legal
    :param expression: The mathematical expression in list form with after conversion of unary minus to tilda
    :return: Raises an exception if operator-operand order is illegal
    """
    for index in range(len(expression)):
        current = expression[index]

        # Checking if exist previous and next elements
        # If one of them does not exist, it will be None (only the first and last elements)
        if index == 0 and index == len(expression) - 1:
            previous_element = None
            next_element = None
        elif index == 0:
            previous_element = None
            next_element = expression[index + 1]
        elif index == len(expression) - 1:
            next_element = None
            previous_element = expression[index - 1]
        else:
            previous_element = expression[index - 1]
            next_element = expression[index + 1]

        # If the element is a number
        if type(current) == float:
            check_number(current, previous_element, next_element)

        # If the element is an operator which is not a bracket
        elif current != '(' and current != ')':
            if Config.position[current] == "mid":
                operator_operand_order_mid(current, previous_element, next_element)
            elif Config.position[current] == "right":
                operator_operand_order_right(current, previous_element, next_element)
            else:
                operator_operand_order_left(current, previous_element, next_element)

        # If the element is a bracket
        else:
            operator_operand_order_brackets(current, previous_element, next_element)


def validate_and_convert(expression: str) -> list:
    """
    Checks validation and converts the mathematical expression to an easier expression to calculate
    :param expression: The given mathematical expression
    :return: Raises an exception if there are illegal elements in the given expression
    """
    try:
        # Removes all white spaces from the mathematical expression
        infix_expression = Convert.remove_white_spaces(expression)

        # Checks if all the elements in the given expression are legal elements
        check_legal_elements(infix_expression)

        # Checks if the amount of opening bracket is equal to the amount of closing brackets
        amount_of_bracket(infix_expression)

        # Checks if after a tilda there is another tilda before a number comes
        check_tilda(infix_expression)

        # Converts all the chars which contain a number to the true float number.
        infix_expression_list = Convert.convert_chars_to_numbers(infix_expression)

        # Checks if operator-operand order is legal
        operator_operand_order(infix_expression_list)

        # Switches unary minuses to a tilda and convert even amount of '-' to '+' according to way number 2
        infix_expression_list = Convert.unary_minus_to_tilda(infix_expression_list)
        return infix_expression_list

    except Exceptions.EmptyExpressionException as eee:
        print(str(eee))
    except Exceptions.OnlyWhiteSpacesException as owse:
        print(str(owse))
    except Exceptions.IllegalElementException as iee:
        print(str(iee))
    except Exceptions.AmountOfBracketsException as aobe:
        print(str(aobe))
    except Exceptions.TildaInARowException as tiare:
        print(str(tiare))
    except Exceptions.OneDecimalPointException as odpe:
        print(str(odpe))
    except Exceptions.DecimalPointWithoutNumberException as dpwne:
        print(str(dpwne))
    except Exceptions.FirstElementException as fee:
        print(str(fee))
    except Exceptions.LastElementException as lee:
        print(str(lee))
    except Exceptions.PreviousElementException as pee:
        print(str(pee))
    except Exceptions.NextElementException as nee:
        print(str(nee))
