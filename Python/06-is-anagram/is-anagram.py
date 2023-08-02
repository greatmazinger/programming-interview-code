"""
Anagram (not to be confused with palindrome)
This solution simply uses the sorted builtin.
"""

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s2 = "".join(sorted(s))
    t2 = "".join(sorted(t))
    return s2 == t2

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
