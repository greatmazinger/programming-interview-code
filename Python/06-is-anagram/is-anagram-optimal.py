"""
Anagram (not to be confused with palindrome)
This solution uses a preprocessing of a string and is optimal in terms of both
speed and space.

m = len(s), n = len(t)
O(m, n) = m + n
"""

from collections import defaultdict

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    # Preprocess t:
    tdict = defaultdict(int)
    for ch in t:
        tdict[ch] += 1
    for ch in s:
        if ch in tdict and tdict[ch] > 0:
            tdict[ch] -= 1
            continue
        return False
    return True

def test1():
    print("Running Test 1:")
    s = "anagrams"
    t = "ganasram"
    assert isAnagram(s, t)
    print(" - Test 1 Success.")

def test2():
    print("Running Test 2:")
    s = "x"
    t = "xyz"
    assert not isAnagram(s, t)
    print(" - Test 2 Success.")

def test3():
    print("Running Test 3:")
    s = "x"
    t = "x"
    assert isAnagram(s, t)
    print(" - Test 3 Success.")

if __name__ == "__main__":
    test1()
    test2()
    test3()
