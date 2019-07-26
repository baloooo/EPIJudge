from test_framework import generic_test


def mul(num1, num2):
    return (num1 * num2)

def add(num1, num2):
    return (num1 + num2)

def sub(num1, num2):
    return (num1 - num2)

def div(num1, num2):
    return (num1 / num2)

def evaluate(expr):
    # TODO - you fill in here.
    '''
    '''
    if not expr:
        return
    expr_list = expr.split(',')
    if len(expr_list) == 1:
        return int(expr)
    op_to_method = {
        '+': add,
        '*': mul,
        '-': sub,
        '/': div
    }
    rpn_stack = []
    for item in expr_list:
        if item in op_to_method:
            num2, num1 = int(rpn_stack.pop()), int(rpn_stack.pop())
            rpn_stack.append(int(op_to_method[item](num1, num2)))
        else:
            rpn_stack.append(item)
    return rpn_stack[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
