from test_framework import generic_test
from test_framework.test_failure import TestFailure

'''
enq: a
enq: b
enq: c
enq: d
deq: 
deq
enq
deq
deq
deq
deq
deq

input: a, b, c
capa = 4
rem_size = 2
head = -1
tail = 2
[a, b, c]
'''

class Queue:
    def __init__(self, capacity):
        # TODO - you fill in here.
        self.rem_size = self.capacity = capacity
        # FIFO: Insert from tail, remove from head
        self.head = self.tail = -1
        self.circular_q = [None]*capacity

    def enqueue(self, x):
        # TODO - you fill in here.
        if self.rem_size != 0: # self.head
            self.tail = (self.tail + 1) % self.capacity
            self.circular_q[self.tail] = x
            self.rem_size -= 1
        else:
            # dynamically resize
            self.rem_size += self.capacity
            self.capacity += self.capacity
            self.circular_q += ([None]*self.capacity)
            self.enqueue(x)

    def dequeue(self):
        # TODO - you fill in here.
        if self.circular_q[self.head] == None:
            return
            #raise Exception('Queue is empty')
        else:
            self.head = (self.head + 1) % self.capacity
            x = self.circular_q[self.head]
            self.circular_q[self.head] = None
            self.rem_size += 1
        return x

    def size(self):
        # TODO - you fill in here.
        return self.capacity - self.rem_size
    '''
    [1]
    [513
    '''


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure(
                    "Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("circular_queue.py",
                                       'circular_queue.tsv', queue_tester))
