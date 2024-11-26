import pytest

def roman_value(roman_char):
    match roman_char.upper():
        case 'I':
            return 1
        case 'V':
            return 5
        case 'X':
            return 10
        case 'L':
            return 50
        case 'C':
            return 100
        case 'D':
            return 500
        case 'M':
            return 1000
        case _:
            return "Caractère invalide"


exemple = "xiiiv"


def roman_to_integer(roman) -> int:
    if len(roman) < 0:
        return 0
    
    value = 0

    for i in range(len(roman)-1):
        if roman_value(roman[i]) < roman_value(roman[i+1]):
            value -= roman_value(roman[i])
        else:
            value += roman_value(roman[i])

    value += roman_value(roman[-1])

    return value


print(roman_to_integer(exemple))
