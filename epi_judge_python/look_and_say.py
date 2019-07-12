from test_framework import generic_test
'''
1, 11, 21, 1211, 111221,
'''


def look_and_say(n):
    # TODO - you fill in here.
    target_num = '1'
    for _ in range(n-1):
        cur_num, cur_num_count = target_num[0], 1
        cur_num_repr = []
        for digit_idx in range(1, len(target_num)):
            if target_num[digit_idx] == cur_num:
                cur_num_count += 1
            else:
                cur_num_repr.append(str(cur_num_count))
                cur_num_repr.append(cur_num)

                cur_num = target_num[digit_idx]
                cur_num_count = 1

        cur_num_repr.append(str(cur_num_count))
        cur_num_repr.append(cur_num)
        target_num = ''.join(cur_num_repr)

    return target_num


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("look_and_say.py", "look_and_say.tsv",
                                       look_and_say))
