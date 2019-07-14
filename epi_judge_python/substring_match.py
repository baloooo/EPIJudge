from test_framework import generic_test

'''
A good string search algorithm is fundamental to the performance of many applications. Several
clever algorithms have been proposed for string search, each with its own trade-offt. As a result,
there is no single perfect answer. If someone asks you this question in an interview, the best way
to approach this problem would be to work through one good algorithm in detail and discuss at a
high level other algorithms.
79
Given two strings s (the "search string") and f (the "text"), find the first occurrence of s in f
'''

def rabin_karp(t, s):
    # TODO - you fill in here.
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("substring_match.py",
                                       'substring_match.tsv', rabin_karp))
