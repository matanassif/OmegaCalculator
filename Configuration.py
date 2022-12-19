# Configuration File which contains all the global constants

import Arithmetic_Functions as Arithmetics

# A dictionary of every operator and its priority
priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '%': 4, '$': 5, '&': 5, '@': 5, '~': 6, '!': 6, '#': 6, '(': 7}

# A dictionary of every operator and its function
arithmetic_function = {'+': Arithmetics.add, '-': Arithmetics.sub, '*': Arithmetics.mul, '/': Arithmetics.div,
                       '^': Arithmetics.power, '%': Arithmetics.modulo, '$': Arithmetics.maximum,
                       '&': Arithmetics.minimum, '@': Arithmetics.average, '~': Arithmetics.negative,
                       '!': Arithmetics.factorial, '#': Arithmetics.add_digits}

# A dictionary of every operator and its position
position = {'+': "mid", '-': "mid", '*': "mid", '/': "mid", '^': "mid", '%': "mid", '$': "mid",
            '&': "mid", '@': "mid", '~': "left", '!': "right", '#': "right", '(': None, ')': None}

# A list of all white spaces
white_spaces = [" ", "\t", "\n", "\v", "\r", "\f"]

# A list of all legal elements in the given mathematical expression
legal_elements = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ' ', '+', '-', '*', '/', '^', '%', '$', '&',
                  '@', '~', '!', '#', '(', ')']

# A list of all legal operators
operators = ['+', '-', '*', '/', '^', '%', '$', '&', '@', '~', '!', '#', '(', ')']

# A list of all the operators which allowed to be in the beginning of the expression
beginning_operators = ['-', '~', '(']

# A list of all the operators which allowed to be in the end of the expression
end_operators = ['!', '#', ')']

# A list of all the operators which allowed to be in next to in a row
in_a_row_operators = ['-', '!']
