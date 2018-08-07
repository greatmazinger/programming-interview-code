import unittest

def length_of_longest_substring(s): 
    """ 
    :type s: str
    :rtype: int
    """
    if len(s) <= 1:
        return len(s)
    result = []
    cur_max = 1 
    cur = 0 
    last = 1 
    done = False
    while not done:
        seen = set(s[cur:last])
        # Start at x until we find a dupe
        if s[last] not in seen:
            seen.add(s[last])
            last += 1
            cur_max = max(cur_max, len(seen))
        else:
            # Found a dupe.
            # Given that s[x:last] where y in [x:last] and s[y] == s[last],
            # Let x = y + 1 -- that is, since s[y] is a repeat at s[last], we
            #    have to start at s[y + 1] and we know it's valid until s[last].
            #    So we can start at s[y + 1:last + 1]
            while (s[cur] != s[last]) and (cur <= last):
                cur += 1
            cur += 1
            if cur == last:
                last += 1
        if last >= len(s) or cur >= len(s):
            done = True
    return cur_max

class test_longest_substring_no_repeat(unittest.TestCase):
    def test_one(self):
        self.assertEqual(length_of_longest_substring("abcabcbb"), 3)

    def test_two(self):
        self.assertEqual(length_of_longest_substring("bbbbbb"), 1)

    def test_three(self):
        self.assertEqual(length_of_longest_substring("pwwkew"), 3)


if __name__ == "__main__":
    import argparse

    # parser = argparse.ArgumentParser(description='Get length of longest substring without repeating characters.')
    # parser.add_argument( 'strings',
    #                      metavar = 'S',
    #                      type = str,
    #                      nargs = 2, # Use "*" for optional? TODO
    #                      help = 'strings to compare' )
    # args = parser.parse_args()
    test = True
    if test:
        print "Longest substring without repeating characters:"
        unittest.main()
    else:
        # Do the args passed in. TODO
        # print str(one_edit_apart)
        pass

