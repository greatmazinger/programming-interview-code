def isPalindrome(s: str) -> bool:
    snew = "".join([x for x in s if x.isalnum()])
    snew = snew.upper()
    return _isPalindromeUpper(snew)

def _isPalindromeUpper(snew: str) -> bool:
    if len(snew) == 0 or len(snew) == 1:
        return True
    return snew[0] == snew[-1] and isPalindrome(snew[1:-1])


def test1():
    print("Running TEST 1:")
    s = "A man, a plan, a canal: Panama"
    assert isPalindrome(s)
    print("- TEST 1 successful.")


if __name__ == "__main__":
    test1()
