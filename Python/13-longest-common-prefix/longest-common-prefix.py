from typing import List
from functools import reduce

def longestCommonPrefix(strs: List[str]) -> str:
    # Get length of shortest
    shortest = min([len(x) for x in strs])
    print(f"DBG: shortest={shortest}")
    lcp = []
    for i in range(shortest):
        anchor = strs[0][i] # ith letter of first word
        is_common = reduce(lambda a, b: a and b, [ s[i] == anchor for s in strs ])
        if is_common:
            lcp.append(anchor)
        else:
            break
    return "".join(lcp)

def test1():
    print("Running TEST 1:")
    strs = ["flower","flow","flight"]
    exp = "fl"

    result = longestCommonPrefix(strs)
    print(f"TEST 1: exp={exp}, result={result}")
    assert exp == result
    print("TEST 1 success.")

def test2():
    print("Running TEST 2:")
    strs = ["abc","ab","abc", "ab", "abc","ab","abc", "ab", "abcdefg"]
    exp = "ab"

    result = longestCommonPrefix(strs)
    print(f"TEST 2: exp={exp}, result={result}")
    assert exp == result
    print("TEST 2 success.")

def test3():
    print("Running TEST 3:")
    strs = ["abc","ab","abc", "ab", "abc","ab","abc", "ab", "xabcdefg"]
    exp = ""

    result = longestCommonPrefix(strs)
    print(f"TEST 3: exp={exp}, result={result}")
    assert exp == result
    print("TEST 3 success.")


if __name__ == "__main__":
    test1()
    test2()
    test3()
