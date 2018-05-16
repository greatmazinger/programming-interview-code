import fileinput

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


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Check if two strings are one edit apart.')
    parser.add_argument( 'strings',
                         metavar = 'S',
                         type = str,
                         nargs = 2,
                         help = 'strings to compare')
    args = parser.parse_args()
