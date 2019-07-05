import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

'''
'alice likes bob'
'bob likes alice'
'''

# Assume s is a string encoded as bytearray.
def reverse_words(s):
    # TODO - you fill in here.
    # plain reverse the entire s
    start, end = 0, len(s)-1
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    # reverse each individual word
    word_start = word_end = 0
    while word_end < len(s):
        if s[word_end] == 32:
            start, end = word_start, word_end-1
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            word_start = word_end + 1
        word_end += 1
    else:
        start, end = word_start, word_end-1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    return


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = bytearray()
    s_copy.extend(map(ord, s))

    executor.run(functools.partial(reverse_words, s_copy))

    return s_copy.decode("utf-8")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_words.py", 'reverse_words.tsv',
                                       reverse_words_wrapper))
