from test_framework import generic_test

'''
For example, if the mangled string is "19216811." then two corresponding IP addresses are
192.168.1.1 and 19.21,6.81.1. (There are seven other possible IP addresses for this string.)
'''

def get_valid_ip_address(ip):
    # TODO - you fill in here.
    '''
    [2, 5, 5, 2, 5, 5, 2, 5, 5]
    '''
    def is_valid_octet(octet):
        try:
            return True if octet == str(int(octet)) and 0 <= int(octet) <= 255 else False
        except Exception:
            pass

    valid_ips = []
    for first_octet_idx in range(1, 4):
        first_octet = ip[:first_octet_idx]
        if not is_valid_octet(first_octet):
            continue
        for second_octet_idx in range(first_octet_idx + 1, first_octet_idx + 4):
            second_octet = ip[first_octet_idx: second_octet_idx]
            if not is_valid_octet(second_octet):
                continue
            for third_octet_idx in range(second_octet_idx + 1, second_octet_idx + 4):
                third_octet = ip[second_octet_idx: third_octet_idx]
                if not is_valid_octet(third_octet):
                    continue
                fourth_octet = ip[third_octet_idx:]
                if not is_valid_octet(fourth_octet):
                    continue

                valid_ips.append(first_octet + '.' + second_octet + '.' + third_octet + '.' + fourth_octet)

    return valid_ips

def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "valid_ip_addresses.py",
            'valid_ip_addresses.tsv',
            get_valid_ip_address,
            comparator=comp))
