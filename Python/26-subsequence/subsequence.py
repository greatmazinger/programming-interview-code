def isSubsequence(s: str, t: str) -> bool:
    sptr = 0
    tptr = 0
    if len(s) > len(t):
        return False
    if len(s) == 0:
        return True
    while sptr < len(s) and tptr < len(t):
        if s[sptr] == t[tptr]:
            sptr += 1
            if sptr == len(s):
                return True
        tptr += 1
    return False

def test1():
    print("Running TEST1:")
    s = "acf"
    t = "abcdefgh"
    assert isSubsequence(s, t)
    print(" - TEST1 successful.")

def test2():
    print("Running TEST2:")
    s = ""
    t = "abcdefgh"
    assert isSubsequence(s, t)
    print(" - TEST2 successful.")

def test3():
    print("Running TEST3:")
    s = "abcdefgh"
    t = "abcdefg"
    assert not isSubsequence(s, t)
    print(" - TEST3 successful.")


if __name__ == "__main__":
    test1()
    test2()
    test3()
