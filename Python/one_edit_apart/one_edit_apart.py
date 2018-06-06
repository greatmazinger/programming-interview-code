import fileinput
import unittest

"""
One Edit Apart function tester.

An edit is:
    Inserting one character anywhere in the word (including at the beginning and end)
    Removing one character
    Replacing one character
    Examples:
        one_edit_apart("cat", "dog") = false 
        one_edit_apart("cat", "cats") = true
        one_edit_apart("cat", "cut") = true
        one_edit_apart("cat", "cast") = true
        one_edit_apart("cat", "at") = true
        one_edit_apart("cat", "act") = false
"""
def one_edit_apart(first = None, second = None):
    if first is None or second is None:
        return False
    # Type check
    elif not isinstance(first, str) or not isinstance(second, str):
        return False
    # Len check
    elif abs(len(first) - len(second)) > 1:
        return False
    elif len(first) == len(second):
        # In this case a letter may only be replaced. Thus there can
        # only be one letter that's different
        i = 0
        diffs = 0
        while i < len(first):
            diffs = (diffs + 1) if first[i] != second[i] else diffs
            i += 1
        return diffs <= 1
    else:
        # In this case a letter may only be added or removed. From one_edit_apart-ness,
        # these are equivalent.
        i = 0
        j = 0
        diffs = 0
        if len(first) < len(second):
            short = first
            longer = second
        else:
            short = second
            longer = first
        while (diffs <= 1) and (i < len(short)):
            if short[i] != longer[j]:
                # Should be removed
                diffs += 1
                # Only increment the longer one because we are removing from longer
                j += 1
                continue
            else:
                j += 1
                i += 1
        return diffs <= 1

class test_one_edit_apart(unittest.TestCase):
    def test_one(self):
        self.assertFalse(one_edit_apart("cat", "dog"))

    def test_two(self):
        self.assertTrue(one_edit_apart("cat", "cats"))

    def test_three(self):
        self.assertTrue(one_edit_apart("cat", "cut"))

    def test_four(self):
        self.assertTrue(one_edit_apart("cat", "cast"))

    def test_five(self):
        self.assertTrue(one_edit_apart("cat", "at"))

    def test_six(self):
        self.assertFalse(one_edit_apart("cat", "act"))

    def test_seven(self):
        self.assertFalse(one_edit_apart(None, "act"))

    def test_eight(self):
        self.assertTrue(one_edit_apart("", ""))

    def test_nine(self):
        self.assertTrue(one_edit_apart("", "x"))

    def test_ten(self):
        self.assertFalse(one_edit_apart(1234, "x"))

    def test_eleven(self):
        self.assertFalse(one_edit_apart("c", "cat"))

if __name__ == "__main__":
    import argparse

    # parser = argparse.ArgumentParser(description='Check if two strings are one edit apart.')
    # parser.add_argument( 'strings',
    #                      metavar = 'S',
    #                      type = str,
    #                      nargs = 2, # Use "*" for optional? TODO
    #                      help = 'strings to compare' )
    # args = parser.parse_args()
    test = True
    if test:
        unittest.main()
    else:
        # Do the args passed in. TODO
        # print str(one_edit_apart)
        pass
