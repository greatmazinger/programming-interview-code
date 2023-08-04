from typing import List

def removeElement(nums: List[int], val: int) -> int:
    # look for not val at end -> cur
    # while not val cur or cur > 0
    # sptr at start, look for val
    # when val found, swap sptr and cur values
    if len(nums) == 0:
        return 0
    sptr = 0
    cur = len(nums) - 1
    while True:
        # starting at cur, look for first non-val
        while cur > 0 and nums[cur] == val:
            cur -= 1
        if cur == 0:
            break
        # cur is pointing to a non-val
        while sptr < cur and nums[sptr] != val:
            sptr += 1
        if (sptr < cur) and nums[sptr] == val:
            nums[sptr] = nums[cur]
            nums[cur] = val
        elif sptr >= cur:
            break
    k = 0
    while k < len(nums) and nums[k] != val:
        k += 1
    return k

def test1():
    print("Running TEST 1:")
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    expected = [ 0, 0, 1, 3, 4]
    k = removeElement(nums, val)
    result = nums[:k]
    result.sort()
    assert  result == expected
    print(" - TEST 1 successful.")


if __name__ == "__main__":
    test1()
