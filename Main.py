# Main file from which the mathematical expression is being get and the result is being returned

import Validation as Valid
import Calculation as Calc


def input_and_validation() -> list:
    """
    Gets the input and checks validation
    :return: A list of the expression in as simpler form
    """
    try:
        mathematical_expression = input("Please enter a mathematical expression:\n")
        return Valid.validate_and_convert(mathematical_expression)
    except EOFError:
        print("End of program")


def main():
    """
    Validates the mathematical expression and calculates the result
    :return: The value of the mathematical expression
    """
    infix_expression_list = input_and_validation()
    if infix_expression_list is not None:
        Calc.calculating(infix_expression_list)
    main()


if __name__ == '__main__':
    main()
