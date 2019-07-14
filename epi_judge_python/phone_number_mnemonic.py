from test_framework import generic_test, test_utils


def get_combinations(phone_number, num_to_char, num_idx, cur_combntn, possible_combntns):
    '''
    Time: 4^n, similar to 2^n for generating binary combinations out of n len strings.
    '''
    # if num_idx == len(phone_number): This condition cannot be used since we'll be ignoring each char once and the num_idx will reach len by ignoring chars also
    if len(cur_combntn) == len(phone_number):
        possible_combntns.append(''.join(cur_combntn))
        return
    for cur_idx in range(num_idx, len(phone_number)):
        for char in num_to_char[phone_number[cur_idx]]:
            cur_combntn.append(char)
            get_combinations(phone_number, num_to_char, cur_idx + 1, cur_combntn, possible_combntns)
            cur_combntn.pop()

def phone_mnemonic(phone_number):
    # TODO - you fill in here.
    '''
    num_to_char = {'0': ['0'], '1': ['1'], '2': ['A', 'B', 'C'], '3': ['D', 'E', 'F'], '4': ['G', 'H', 'I'], '5': ['J', 'K', 'L'], '6': ['M', 'N', 'O'], '7': ['P', 'Q', 'R', 'S'],
                   '8': ['T', 'U', 'V'], '9': ['W', 'X', 'Y', 'Z']}
    possible_combntns = []
    get_combinations(phone_number, num_to_char, 0, [], possible_combntns)
    return possible_combntns
    '''
    letters = ['0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    res = ['']
    for digit in phone_number:
        digit = int(digit)
        res = [prefix + suffix for prefix in res for suffix in letters[digit]]

    return res



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
