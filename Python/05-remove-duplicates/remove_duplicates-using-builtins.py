from typing import List

"""
Remove duplicates using builtin data structure 'set' and list method 'sort'.
So sort of a borderline not following the instructions but still legal way of solving
the problem.
"""

def test1():
    print("Running Test 1:")
    nums = [0,0,1,1,1,2,2,3,3,4]
    expected = [0,1,2,3,4]
    k = removeDuplicates(nums)
    for i in range(len(expected)):
        assert nums[i] == expected[i]
    print(f"DBG: Result = {str(nums)}")
    print(" - Test 1 Success.")

def removeDuplicates(nums: List[int]) -> int:
    result = set(nums)
    result = list(result)
    result.sort()
    nums.clear()
    nums.extend(result)

if __name__ == "__main__":
    test1()
