# Main file from which the mathematical expression is being get and the result is being returned

import Validation as Valid
import Calculation as Calc


def main() -> float:
    """
    Validates the mathematical expression and calculates the result
    :return: The value of the mathematical expression
    """
    mathematical_expression = input("Please and a mathematical expression:\n")
    infix_expression_list = Valid.validate_and_convert(mathematical_expression)
    print(Calc.calculating(infix_expression_list))
    return Calc.calculating(infix_expression_list)


if __name__ == '__main__':
    main()
