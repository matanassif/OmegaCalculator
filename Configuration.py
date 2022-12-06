# Configuration File which contains all the global constants

import Arithmetic_Functions as Arethmetics

# A dictionary of every operator and its priority
priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '%': 4, '$': 5, '&': 5, '@': 5, '~': 6, '!': 6, '#': 6}

# A dictionary of every operator and its function
arithmetic_function = {'+': Arethmetics.add, '-': Arethmetics.sub, '*': Arethmetics.mul, '/': Arethmetics.div,
                       '^': Arethmetics.power, '%': Arethmetics.modulo, '$': Arethmetics.maximum,
                       '&': Arethmetics.minimum, '@': Arethmetics.average, '~': Arethmetics.negative,
                       '!': Arethmetics.factorial, '#': Arethmetics.add_digits}

# A dictionary of every operator and its position
position = {'+': "mid", '-': "mid", '*': "mid", '/': "mid", '^': "mid", '%': "mid", '$': "mid",
            '&': "mid", '@': "mid", '~': "lef", '!': "right", '#': "right"}
