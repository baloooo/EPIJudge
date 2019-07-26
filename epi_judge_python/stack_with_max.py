from test_framework import generic_test
from test_framework.test_failure import TestFailure

'''
[10, 20, 30, 40, 25, 55, 2]

[(10,None), (20, 10), (30, 20), (40, 30), (25, 40), (55, 40), (2, 55)]

max_stack = 40

[(10,None), (20, 10), (30, 20), (40, 30), (25, 40), (55, 40), (2, 55)]

[10, (20, 10), (30, 20), (40, 30), (25, 40), (55, 40), (2, 55)]
[10, 10]
max_stack = 20
pop:
    if max_stack >



[10, 20, 30, 40, -15, 15, -53]
max = 55

arr = [0, 0, 0, 0, 0, 0, 0]
max = 55

while pushing:
    arr.push(key - cur_max)


while getting max:
    cur_ele = cur_max - arr[-1]
'''

class Stack:
    def __init__(self):
        self.stack = []
        self.max_stack = None

    def empty(self):
        # TODO - you fill in here.
        return len(self.stack) == 0

    def max(self):
        # TODO - you fill in here.
        if self.empty():
            return
        return self.max_stack

    def pop(self):
        # TODO - you fill in here.
        if not self.stack:
            return
        key, self.max_stack = self.stack.pop()
        return key

    def push(self, x):
        # TODO - you fill in here.
        self.stack.append((x, self.max_stack))

        if (not self.max_stack) or (x > self.max_stack):
            self.max_stack = x
        return


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("stack_with_max.py",
                                       'stack_with_max.tsv', stack_tester))
