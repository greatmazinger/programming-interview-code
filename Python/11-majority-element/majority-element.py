from collections import Counter, defaultdict
from typing import List

def _judge(nums: List[int]) -> int:
    summary = Counter(nums)
    maj = summary.most_common(1)[0]
    return maj[0]

def majorityElement(nums: List[int]) -> int:
    counts = defaultdict(int)
    goal = len(nums) // 2
    for x in nums:
        counts[x] += 1
        if counts[x] > goal:
            return x

def test1():
    print("Running TEST 1:")
    nums = [3,2,3]
    tgt = _judge(nums)
    result = majorityElement(nums)
    print(f"EXP = {tgt}  RESULT = {result}")
    assert tgt == result
    print("- TEST 1 successful.")

def test2():
    print("Running TEST 2:")
    nums = [2,2,1,1,1,2,2]
    tgt = _judge(nums)
    result = majorityElement(nums)
    print(f"EXP = {tgt}  RESULT = {result}")
    assert tgt == result
    print("- TEST 2 successful.")

def test3():
    print("Running TEST 3:")
    nums = [1] * 999
    nums.extend([2] * 1000)
    tgt = _judge(nums)
    result = majorityElement(nums)
    print(f"EXP = {tgt}  RESULT = {result}")
    assert tgt == result
    print("- TEST 3 successful.")

if __name__ == "__main__":
    test1()
    test2()
    test3()
