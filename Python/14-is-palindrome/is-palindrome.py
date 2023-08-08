def isPalindrome(s: str) -> bool:
    snew = "".join([x for x in s if x.isalnum()])
    snew = snew.upper()
    start = 0
    end = len(snew) # non-inclusive
    length = end
    while end - start >= 0:
        if length == 0 or length == 1:
            return True
        elif snew[start] == snew[end - 1]:
            start += 1
            end -= 1
            length -= 2
        else:
            return False

def test1():
    print("Running TEST 1:")
    s = "A man, a plan, a canal: Panama"
    assert isPalindrome(s)
    print("- TEST 1 successful.")

def test2():
    print("Running TEST 2:")
    s = ", . :   "
    assert isPalindrome(s)
    print("- TEST 2 successful.")

def test3():
    print("Running TEST 3:")
    s = "abcdefg"
    assert not isPalindrome(s)
    print("- TEST 3 successful.")


if __name__ == "__main__":
    test1()
    test2()
    test3()
