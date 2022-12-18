# This file contains the tests of the calculator

import pytest

import Convertion
import Validation
import Calculation
import Exceptions


def test_simple_1():
    mathematical_expression = "2*17%3&7"
    infix_expression_list = Validation.validate_and_convert(mathematical_expression)
    assert Calculation.calculating(infix_expression_list) == 4


def test_simple_2():
    mathematical_expression = "3@47$56"
    infix_expression_list = Validation.validate_and_convert(mathematical_expression)
    assert Calculation.calculating(infix_expression_list) == 56


def test_simple_3():
    mathematical_expression = "14-7!+~65%17"
    infix_expression_list = Validation.validate_and_convert(mathematical_expression)
    assert Calculation.calculating(infix_expression_list) == -5023


def test_simple_4():
    mathematical_expression = "17*8/2^3$7"
    infix_expression_list = Validation.validate_and_convert(mathematical_expression)
    assert Calculation.calculating(infix_expression_list) == 1.0625


def test_simple_5():
    mathematical_expression = "65@84%14*5+6-18/12"
    infix_expression_list = Validation.validate_and_convert(mathematical_expression)
    assert Calculation.calculating(infix_expression_list) == 27


def test_simple_6():
    mathematical_expression = "18/32*23+45#"
    infix_expression_list = Validation.validate_and_convert(mathematical_expression)
    assert Calculation.calculating(infix_expression_list) == 21.9375


def test_simple_7():
    mathematical_expression = "41#/11%10^6+345"
    infix_expression_list = Validation.validate_and_convert(mathematical_expression)
    assert Calculation.calculating(infix_expression_list) == 350


def test_simple_8():
    mathematical_expression = "10600$12!&25900"
    infix_expression_list = Validation.validate_and_convert(mathematical_expression)
    assert Calculation.calculating(infix_expression_list) == 25900


def test_simple_9():
    mathematical_expression = "9*~6^3"
    infix_expression_list = Validation.validate_and_convert(mathematical_expression)
    assert Calculation.calculating(infix_expression_list) == -1944


def test_simple_10():
    mathematical_expression = "~19*5+80+~---------17@~32"
    infix_expression_list = Validation.validate_and_convert(mathematical_expression)
    assert Calculation.calculating(infix_expression_list) == -9.5


def test_simple_11():
    mathematical_expression = "~32*477/~15"
    infix_expression_list = Validation.validate_and_convert(mathematical_expression)
    assert Calculation.calculating(infix_expression_list) == 1017.6


def test_simple_12():
    mathematical_expression = "13^4&512%52+78"
    infix_expression_list = Validation.validate_and_convert(mathematical_expression)
    assert Calculation.calculating(infix_expression_list) == 28639


def test_simple_13():
    mathematical_expression = "47+~988*11!$10065/31"
    infix_expression_list = Validation.validate_and_convert(mathematical_expression)
    assert Calculation.calculating(infix_expression_list) == -1272186998.1612904


def test_complex_1():
    mathematical_expression = "(14^6/ 53@1      7$47#)/ 30"
    infix_expression_list = Validation.validate_and_convert(mathematical_expression)
    assert Calculation.calculating(infix_expression_list) == 7170.986666666667


def test_complex_2():
    mathematical_expression = "(14^6/ 53@1      7$47#)/ 365"
    infix_expression_list = Validation.validate_and_convert(mathematical_expression)
    assert Calculation.calculating(infix_expression_list) == 589.3961643835617


def test_complex_3():
    mathematical_expression = "~((14-7!+~65%17)$(15^3+65%78))"
    infix_expression_list = Validation.validate_and_convert(mathematical_expression)
    assert Calculation.calculating(infix_expression_list) == -3440


def test_complex_4():
    mathematical_expression = " (17*8/2^3  $7)@1589# "
    infix_expression_list = Validation.validate_and_convert(mathematical_expression)
    assert Calculation.calculating(infix_expression_list) == 12.03125


def test_complex_5():
    mathematical_expression = "~54 / (65@84%14*5+6-18/12)"
    infix_expression_list = Validation.validate_and_convert(mathematical_expression)
    assert Calculation.calculating(infix_expression_list) == -2


def test_complex_6():
    mathematical_expression = "~17/5*(12    +6#)+14^2"
    infix_expression_list = Validation.validate_and_convert(mathematical_expression)
    assert Calculation.calculating(infix_expression_list) == 134.8


def test_complex_7():
    mathematical_expression = "385600#/14%13^5+(345&2560)"
    infix_expression_list = Validation.validate_and_convert(mathematical_expression)
    assert Calculation.calculating(infix_expression_list) == 367


def test_complex_8():
    mathematical_expression = "15+~87%(23$8!@430&53200)"
    infix_expression_list = Validation.validate_and_convert(mathematical_expression)
    assert Calculation.calculating(infix_expression_list) == 20303


def test_complex_9():
    mathematical_expression = "(102  +30%(9*~6^3)) *     14"
    infix_expression_list = Validation.validate_and_convert(mathematical_expression)
    assert Calculation.calculating(infix_expression_list) == -25368


def test_complex_10():
    mathematical_expression = "---~   ---14*5+36    +~56@~   345 *(12%78&65)"
    infix_expression_list = Validation.validate_and_convert(mathematical_expression)
    assert Calculation.calculating(infix_expression_list) == -2440


def test_complex_11():
    mathematical_expression = "(~23*14     /~92+55%       32) *69-~23"
    infix_expression_list = Validation.validate_and_convert(mathematical_expression)
    assert Calculation.calculating(infix_expression_list) == 1851.5


def test_complex_12():
    mathematical_expression = "(15^45&8     00%40+ 56)/345%340"
    infix_expression_list = Validation.validate_and_convert(mathematical_expression)
    assert Calculation.calculating(infix_expression_list) == 151886.2


def test_complex_13():
    mathematical_expression = "((1565*556       )%15  6^3 &89)"
    infix_expression_list = Validation.validate_and_convert(mathematical_expression)
    assert Calculation.calculating(infix_expression_list) == 2097152


def test_complex_14():
    mathematical_expression = "(18*      35-~(4 5#+      15) & 85) / 10"
    infix_expression_list = Validation.validate_and_convert(mathematical_expression)
    assert Calculation.calculating(infix_expression_list) == 65.4


def test_complex_15():
    mathematical_expression = "(9   8+~34*17!$80      00  0/32) *15   -15"
    infix_expression_list = Validation.validate_and_convert(mathematical_expression)
    assert Calculation.calculating(infix_expression_list) == -5668768385278545.0


def test_complex_16():
    mathematical_expression = "(5+~-2@6+4@- 5%6^ 5$-8* 2) -9- (-10&8)"
    infix_expression_list = Validation.validate_and_convert(mathematical_expression)
    assert Calculation.calculating(infix_expression_list) == 10063.6875


def test_complex_17():
    mathematical_expression = "(4!-5@3#   +4$- 5%6^ 7@4* 9) -- 10- ~(1352/-14) "
    infix_expression_list = Validation.validate_and_convert(mathematical_expression)
    assert Calculation.calculating(infix_expression_list) == 18365.428571428572


def test_tilda_in_a_row_exception():
    with pytest.raises(Exceptions.TildaInARowException):
        expression_list = Convertion.convert_to_list("~~3")
        assert Validation.check_tilda(expression_list)


def test_more_than_one_decimal_point():
    with pytest.raises(Exceptions.OneDecimalPointException):
        assert Convertion.convert_chars_to_numbers("3.2.5 + 6 *58")


def test_next_element_exception():
    with pytest.raises(Exceptions.NextElementException):
        expression_list = Convertion.convert_to_list("3+*4")
        assert Validation.operator_operand_order(expression_list)


def test_first_element():
    with pytest.raises(Exceptions.FirstElementException):
        expression_list = Convertion.convert_to_list("$5*516&6515@451")
        assert Validation.operator_operand_order(expression_list)


def test_last_element():
    with pytest.raises(Exceptions.LastElementException):
        expression_list = Convertion.convert_to_list("59*45898/564%")
        assert Validation.operator_operand_order(expression_list)


def test_illegal_elements():
    with pytest.raises(Exceptions.IllegalElementException):
        assert Validation.check_legal_elements("hello there")


def test_empty_expression():
    with pytest.raises(Exceptions.EmptyExpressionException):
        assert Convertion.remove_white_spaces("")


def test_only_white_spaces_expression():
    with pytest.raises(Exceptions.OnlyWhiteSpacesException):
        assert Convertion.remove_white_spaces("        ")
