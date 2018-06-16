import fileinput
import unittest

from collections import defaultdict

"""
TODO:
    Examples:
"""
def first_nonrepeated_character(instring):
    cmap = defaultdict(int)
    leftmost_dict = {}
    for index in range(len(instring)):
        char = instring[index]
        if cmap[char] == 0:
            leftmost_dict[char] = index
        cmap[char] += 1
    leftmost_list = [ (char, leftmost_dict[char]) for char in cmap.keys() if cmap[char] == 1 ]
    if len(leftmost_list) == 0:
        return None
    else:
        leftmost = leftmost_list[0]
        for item in leftmost_list[1:]:
            if item[1] < leftmost[1]:
                leftmost = item
        return leftmost[0]

# TODO
class test_first_nonrepeated_character(unittest.TestCase):
    def test_one(self):
        self.assertEqual(first_nonrepeated_character("ccaat"), 't')
    def test_two(self):
        self.assertEqual(first_nonrepeated_character("x"), 'x')


if __name__ == "__main__":
    import argparse

    # parser = argparse.ArgumentParser(description='Find first nonrepeated character in input string.')
    # parser.add_argument( 'instring',
    #                      metavar = 'S',
    #                      type = str,
    #                      help = 'Input string' )
    # args = parser.parse_args()
    test = True
    if test:
        unittest.main()
    else:
        # Do the args passed in. TODO
        result = first_nonrepeated_character( instring = args.instring )
        print(result)
