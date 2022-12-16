# This file contains the functions which convert to postfix and calculates the final result

import Configuration as Config


# The function converts the mathematical expression to a postfix form of expression
def convert_to_postfix(expression: list) -> list:
    """
    Converts the mathematical expression from infix form to postfix form in order to make the calculation simpler
    :param expression: mathematical expression in infix form
    :return: A list which contains the given mathematical expression in postfix form
    """

    # Contains the mathematical expression in postfix form
    postfix_list = list()

    # A temporary list to contain the operators during conversion to postfix
    operators = list()

    for element in expression:

        # If the element is numeric, the element is being inserted to postfix list
        if type(element) == float:
            postfix_list.append(element)

        # If the element is a closing bracket, then all the operators except the last opening bracket will be inserted
        # to the postfix list because every mathematical operation which is in bracket should be done first
        elif element == ')':
            while (len(operators) != 0) and operators[-1] != '(':
                postfix_list.append(operators.pop(-1))

            operators.pop(-1)

        # If the element is an operator which is not a closing bracket, it will be inserted to the operators list after
        # all the operators (which has same or higher priority) will be inserted into the postfix list
        # The reason is that the expression is being calculated from highest priority to lowest priority
        else:
            while len(operators) != 0 and Config.priority[operators[-1]] >= Config.priority[element]:
                if operators[-1] != '(':

                    # If the element is an operator which is positioned from the left, then it should be added after
                    # there is at least one number in the list, since only a number can be in index 0 in postfix
                    if element in Config.operators and Config.position[element] == "left" and len(postfix_list) == 0:
                        break
                    else:
                        postfix_list.append(operators.pop(-1))
                else:
                    break

            operators.append(element)

    while len(operators) != 0:
        postfix_list.append(operators.pop(-1))

    return postfix_list


def calculate_postfix(expression: list) -> float:
    """
    Calculates the postfix form of the  mathematical expression from left to right because in postfix the order declares
    which operation should to happen first
    :param expression: mathematical expression in postfix form
    :return: The result of the given mathematical expression
    """
    # List which contains the results of the calculations along the main calculation and contains the result in the end
    operands = list()

    for element in expression:

        # If the element is numeric it inserts it to the operand list
        if type(element) == float:
            operands.append(element)

        # If the operator should have two operands (meaning the position of the operand in "mid"), it removes two
        # operands from the operand list and activates the arithmetic operation on them.
        # Otherwise, it removes only one operand and activates the arithmetic operation on it.
        # Finally it inserts the result to the operand list
        else:
            first_operand = operands.pop(-1)
            if Config.position[element] != "mid":
                result = Config.arithmetic_function[element](first_operand)

            else:
                second_operand = operands.pop(-1)
                result = Config.arithmetic_function[element](second_operand, first_operand)

            operands.append(result)

    return operands.pop(-1)


def calculating(expression: list) -> float:
    """
    Converts the mathematical expression from infix form to postfix form in order to make the calculation simpler
    and then calculates it
    :param expression: mathematical expression in infix form
    :return: Result of the mathematical expression
    """
    postfix_form = convert_to_postfix(expression)
    return calculate_postfix(postfix_form)
