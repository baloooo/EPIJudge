from test_framework import generic_test


'''
[a, b, c, d]
|  |
| d|
| c|
| b|
|_a|
'''

class Queue:
    def __init__(self):
        self.stack = []

    def enqueue(self, x):
        # TODO - you fill in here.
        self.stack.append(x)
        return

    def dequeue(self):
        # TODO - you fill in here.
        # Pop stack to a temp stack
        temp_stack = []
        while self.stack:
            temp_stack.append(self.stack.pop())
        ele_to_deq = temp_stack.pop()
        while temp_stack:
            self.stack.append(temp_stack.pop())
        return ele_to_deq


def queue_tester(ops):
    from test_framework.test_failure import TestFailure

    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure("Dequeue: expected " + str(arg) +
                                      ", got " + str(result))
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("queue_from_stacks.py",
                                       'queue_from_stacks.tsv', queue_tester))
