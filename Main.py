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
        return Valid.catch_exceptions(mathematical_expression)
    except EOFError:
        print("End of program")


def main():
    """
    Validates the mathematical expression and calculates the result
    :return: The value of the mathematical expression
    """
    while True:
        infix_expression_list = input_and_validation()
        if infix_expression_list is not None and type(infix_expression_list) != str:
            Calc.calculating(infix_expression_list)
        # If the there is an exception which is not EOF
        elif infix_expression_list is not None and type(infix_expression_list) == str:
            print(infix_expression_list)
            continue
        else:
            break


if __name__ == '__main__':
    main()
