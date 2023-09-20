
def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    if len(s) == 0:
        return True
    if s == t:
        return True
    lookup = {}
    reverse = {}
    for i in range(len(s)):
        if s[i] not in lookup:
            if t[i] in reverse:
                return False
            lookup[s[i]] = t[i]
            reverse[t[i]] = s[i]
        else:
            if lookup[s[i]] != t[i]:
                return False
    return True

def test1():
    print("Running TEST1:")
    s = "egg"
    t = "add"
    assert isIsomorphic(s, t)
    print(" - TEST1 successful.")

def test2():
    print("Running TEST2:")
    s = "foo"
    t = "bar"
    assert not isIsomorphic(s, t)
    print(" - TEST2 successful.")

def test3():
    print("Running TEST3:")
    s = "paper"
    t = "title"
    assert isIsomorphic(s, t)
    print(" - TEST3 successful.")

def test4():
    print("Running TEST4:")
    s = "papers"
    t = "titlee"
    assert not isIsomorphic(s, t)
    print(" - TEST4 successful.")

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
