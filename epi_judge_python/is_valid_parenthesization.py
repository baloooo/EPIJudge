from test_framework import generic_test

'''
A string over the characters " l,l ,O,l,l" is said to be well-formed if the different types of brackets
match in the correct order.
For example, "(UXQ)" is well-formed, as is "[0t]{00}]". However, "{)", "0", and "[0[]{00" are
not well-formed,
Write a program that tests if a string made up of the characters '(', ')' ,'I' ,'l' /'l' and")' is well-formed,
'''

def is_well_formed(s):
    # TODO - you fill in here.
    close_to_open_paran_map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    paran_stack = []
    for ch in s:
        if ch in close_to_open_paran_map:
            try:
                matching_opening_paran = paran_stack.pop()
            except Exception:
                return False
            if matching_opening_paran != close_to_open_paran_map[ch]:
                return False
        else:
            paran_stack.append(ch)
    return True if len(paran_stack) == 0 else False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_parenthesization.py",
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
