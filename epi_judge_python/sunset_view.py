from test_framework import generic_test

'''
You are given a series of buildings that have windows facing west. The buildings are in a straight
line, and any building which is to the east of a building of equal or greater height cannot view the
sunset.
103
Design an algorithm that processes buildings in east-to-west order and returns the set of buildings
which view the sunset. Each building is specified by its height.

2 3 4 5 2 3
input ele in to stack (traversing form right to left), 
if tos > cur:
    push cur
else:
    pop tos

by the end of the day elements in the stack are the buildings which can see the sunset

'''

def examine_buildings_with_sunset(sequence):
    # TODO - you fill in here.
    candidates_stack = []
    '''
    [2, 3, 4, 5, 2, 3]
    
    (2, 5)
    
    (1, 2)
    (0, 3)
    '''
    for bldng_id in range(len(sequence)):
        bldng_height = sequence[bldng_id]
        if not candidates_stack or bldng_height <= candidates_stack[-1][1]:
            candidates_stack.append((bldng_id, bldng_height))
        else:
            while candidates_stack and bldng_height > candidates_stack[-1][1]:
                candidates_stack.pop()
            candidates_stack.append((bldng_id, bldng_height))
    return [candidate[0] for candidate in reversed(candidates_stack)]


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sunset_view.py", 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
