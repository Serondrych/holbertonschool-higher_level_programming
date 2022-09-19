#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for i in range(len(roman_string)):
        if roman.get(roman_string[i], 0) == 0:
            return (0)

        if (i != (len(roman_string) - 1) and
            roman[roman_string[i]] < roman[roman_string[i + 1]]):
            num += roman[roman_string[i]] * -1

        else:
            num += roman[roman_string[i]]
    return (num)
