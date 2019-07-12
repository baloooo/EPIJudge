from test_framework import generic_test
from test_framework.test_failure import TestFailure

'''
"aaaabcccaa" is "4a1b3c2a".
The decoding of "3e4f2e" refurns "eeeffffee".
'''

def chunker(target_str, size):
    return [target_str[pos: pos+size] for pos in range(0, len(target_str), size)]

def decoding(s):
    # TODO - you fill in here.
    if not s:
        return ''
    decoded_str = []
    cur_char_idx = 0
    while cur_char_idx < len(s):
        count_idx = orig_char_idx = cur_char_idx
        while count_idx < len(s) and s[count_idx].isdigit():
            count_idx += 1
        count = int(s[orig_char_idx:count_idx])
        decoded_str.append(s[count_idx] * count)
        cur_char_idx = count_idx + 1

    return ''.join(decoded_str)


def encoding(s):
    # TODO - you fill in here.
    if not s:
        return ''
    cur_ch, count = s[0], 1
    encoded_str = []
    for ch_idx in range(1, len(s)):
        ch = s[ch_idx]
        if ch == cur_ch:
            count += 1
        else:
            encoded_str.append(str(count))
            encoded_str.append(cur_ch)
            cur_ch, count = ch, 1

    encoded_str.append(str(count))
    encoded_str.append(cur_ch)
    return ''.join(encoded_str)


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("run_length_compression.py",
                                       'run_length_compression.tsv',
                                       rle_tester))
