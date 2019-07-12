from test_framework import generic_test

'''
For example, if the mangled string is "19216811." then two corresponding IP addresses are
192.168.1.1 and 19.21,6.81.1. (There are seven other possible IP addresses for this string.)

1 1 1 max
1 1 2 max
1 1 3 max

2 1 1 max
2 1 2 max


3 3 3 max
3 3 2 max
3 3 1 max

2 3 max
2 2 max
2 1 max

1 3 max
1 2 max
1 1 max
'''

def within_range(octet):
    try:
        return True if 0 <= int(octet) <= 255 else False
    except Exception:
        return False

def get_valid_ip_address(ip):
    # TODO - you fill in here.
    # first do recursive bruteforce
    possible_ips = []
    for first_octet_idx in range(4):
        first_octet = ip[:first_octet_idx + 1]
        if not within_range(first_octet):
            continue
        # print('first_octet:', first_octet)
        for second_octet_idx in range(first_octet_idx + 1, first_octet_idx + 4):
            second_octet = ip[first_octet_idx + 1: second_octet_idx + 1]
            if not within_range(second_octet):
                continue
            # print('second octet is', second_octet)
            for third_octet_idx in range(second_octet_idx + 1, second_octet_idx + 4):
                third_octet = ip[second_octet_idx + 1: third_octet_idx + 1]
                # print('third octet is', third_octet)
                if not within_range(third_octet):
                    continue
                fourth_octet = ip[third_octet_idx + 1:]
                # print('fourth octet is ', fourth_octet)
                if not within_range(fourth_octet):
                    continue
                possible_ips.append(first_octet + '.' + second_octet + '.' + third_octet + '.' + fourth_octet)
    # next do iterative version
    return possible_ips


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "valid_ip_addresses.py",
            'valid_ip_addresses.tsv',
            get_valid_ip_address,
            comparator=comp))
