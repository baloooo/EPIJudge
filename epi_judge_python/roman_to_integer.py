from test_framework import generic_test


def roman_to_integer(s):
    # TODO - you fill in here.
    roman_to_integer_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    'X X I V'
    final_int = 0
    for idx in range(len(s)-1, -1, -1):
        if idx != len(s)-1 and roman_to_integer_map[s[idx]] < roman_to_integer_map[s[idx + 1]]:
            final_int -= roman_to_integer_map[s[idx]]
        else:
            final_int += roman_to_integer_map[s[idx]]
    return final_int


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "roman_to_integer.py", 'roman_to_integer.tsv', roman_to_integer))
