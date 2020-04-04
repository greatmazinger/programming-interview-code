import unittest

from collections import Counter 

"""
No repeating digits problem:
    Examples:
"""

limit = 98765432100

def no_repeating_digits(num):
    num_str = str(num)
    c = Counter(list(num_str))
    most_common = c.most_common(1)
    return most_common[0][1] == 1

def count_non_repeating_numbers(low, high):
    total = 0
    cur = low
    while cur <= high and cur <= limit:
        if no_repeating_digits(cur):
            total += 1
        cur += 1
    return total

# TODO
# class test_first_nonrepeated_character(unittest.TestCase):
#     def test_one(self):
#         self.assertEqual(first_nonrepeated_character("ccaat"), 't')
#     def test_two(self):
#         self.assertEqual(first_nonrepeated_character("x"), 'x')


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Count number of numbers that don't have repeating digits.")
    parser.add_argument( 'n1',
                         metavar = 'N1',
                         type = int,
                         help = 'Left number (inclusive)' )
    parser.add_argument( 'n2',
                         metavar = 'N2',
                         type = int,
                         help = 'Right number (inclusive)' )
    args = parser.parse_args()
    test = False
    if test:
        unittest.main()
    else:
        # Do the args passed in. TODO
        result = count_non_repeating_numbers( args.n1, args.n2 )
        print(result)
