from test_framework import generic_test

'''

1,2,3
1,3,2
2,1,3
2,3,1
3,1,2
3,2,1

1,2,3,4,5
1,2,3,5,4
1,2,4,3,5
1,2,4,5,3

'''

def next_permutation(perm):
    # TODO - you fill in here.
    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "next_permutation.py", 'next_permutation.tsv', next_permutation))
