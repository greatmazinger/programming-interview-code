from typing import List

def isPalindromeList(q: List) -> bool:
    length = len(q)
    if length == 0 or length == 1:
        return True
    for ind in range(length // 2):
        if q[ind] != q[length - ind -1]:
            return False
    return True

def isPalindrome(x: int) -> bool:
    slist = []
    y = abs(x)
    while y > 0:
        rem = y % 10
        y = y // 10
        slist.append(rem)
    if x < 0:
        slist.append('-')
    slist.reverse()
    return isPalindromeList(slist)

def test1():
    print("Running TEST 1:")
    x = 121
    assert isPalindrome(x)
    print(" - TEST 1 successful.")

def test2():
    print("Running TEST 2:")
    x = -121
    assert not isPalindrome(x)
    print(" - TEST 2 successful.")

def test3():
    print("Running TEST 3:")
    x = -123421
    assert not isPalindrome(x)
    print(" - TEST 3 successful.")

if __name__ == "__main__":
    test1()
    test2()
    test3()
