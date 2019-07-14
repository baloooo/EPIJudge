from test_framework import generic_test

'''
We illustrate what it means to write a shing in sinusoidal fashionby means of an example. The string
e-I
"Hello-World!" written in sinusoidal fashion is H I o I{ r d
1o!
(Here - denotes ablank.)
Define the snakestring of s to be the left-right top-to-bottom sequence in which characters appear
when s is written in sinusoidal fashion. For example, the snakestring string for "Hello-World!" is
"e-lHloWrdlo!".
Write a program which takes as input a string s and retums the snakestring of s'
'''

def snake_string(s):
    # TODO - you fill in here.
    # The sol in the book takes O(3n) time, though simpler for coding this one is more efficient.
    arr = [[], [], []]
    idx, direction_up = 1, False
    for ch in s:
        if idx in [-1, 3]:
            idx = 1
            direction_up = not direction_up
        arr[idx % 3].append(ch)
        if direction_up:
            idx += 1
        else:
            idx -= 1
    return ''.join(arr[0] + arr[1] + arr[2])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("snake_string.py", 'snake_string.tsv',
                                       snake_string))
