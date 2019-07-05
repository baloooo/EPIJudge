from test_framework import generic_test
'''
Spreadsheets often use an alphabetical encoding of the successive columns. Specifically, columns
areidentifiedby"N',"8","C",,,,,"X","Y","2","AN',"A8",.,.,"22","AAN',"4A8",.,..
Implement a function that converts a spreadsheet column id to the corresponding integeq, with" N'
corresponding to 1. For example, you should retum 4 for "D" ,27 for " AN' ,702 for "ZZ" , elc. How
would you test your code?
'''


def ss_decode_col_id(col):
    # TODO - you fill in here.
    import string
    id_to_num = dict(zip(string.ascii_uppercase, list(range(1, 27))))
    power = len(col) - 1
    col_id = 0
    for ch in col:
        col_id += (id_to_num[ch] * (26 ** power))
        power -= 1
    return col_id


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spreadsheet_encoding.py",
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
