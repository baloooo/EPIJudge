from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number):
    # TODO - you fill in here.
    num_to_char = {0: [''], 1: ['A', 'B', 'C'], 2: ['D', 'E', 'F'], 3: ['G', 'H', 'I'], 4: ['J', 'K', 'L'], 5: ['M', 'N', 'O'], 6: ['P]']}
    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
