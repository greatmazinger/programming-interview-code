from typing import List

def removeDuplicates(nums: List[int]) -> int:
    cur = 1
    for x in range(1, len(nums)):
        if nums[x] != nums[cur - 1]:
            nums[cur] = nums[x]
            cur = cur + 1
    return cur

def test1():
    print("Running Test 1:")
    nums = [0,0,1,1,1,2,2,3,3,4]
    expected = [0,1,2,3,4]
    k = removeDuplicates(nums)
    for i in range(len(expected)):
        assert nums[i] == expected[i]
    print(f"DBG: Result = {str(nums)}")
    print(" - Test 1 Success.")
if __name__ == "__main__":
    test1()
