from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x):
    # TODO - you fill in here.
    if x == 0:
        return '0'
    sign = False
    if x < 0:
        sign = True
    x = abs(x)
    char_list = []
    while x > 0:
        quot, rem = divmod(x, 10)
        char_list.append(str(rem))
        x = quot
    str_repr = ''.join(reversed(char_list))
    return str_repr if not sign else '-' + str_repr


def string_to_int(s):
    # TODO - you fill in here.
    if len(s) == 0: return ''
    sign = False
    if s[0] == '-':
        sign = True
        s = s[1:]
    int_equivalent = 0
    unit_place = len(s) - 1
    for ch in s:
        int_equivalent += (int(ch) * (10 ** unit_place))
        unit_place -= 1
    return int_equivalent if not sign else -1 * int_equivalent


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
       generic_test.generic_test_main("string_integer_interconversion.py",
                                      'string_integer_interconversion.tsv',
                                      wrapper))
