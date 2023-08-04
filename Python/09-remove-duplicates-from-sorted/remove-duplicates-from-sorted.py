from typing import List

def removeDuplicates(nums: List[int]) -> int:
    ptr = 0
    save = 0
    length = len(nums)
    while ptr < length:
        found = 0
        cur = nums[ptr]
        while ptr < length and nums[ptr] == cur:
            ptr += 1
            found += 1
        nums[save] = cur
        save += 1
        if found > 1 and save < length:
            nums[save] = cur
            save += 1
    return save

def test1():
    print("Running Test 1:")
    nums = [0,0,1,1,1,2,3,3,4]
    expected = [0,0,1,1,2,3,3,4]
    k = removeDuplicates(nums)
    for i in range(len(expected)):
        assert nums[i] == expected[i]
    print(f"DBG: Result = {str(nums)}")
    print(" - Test 1 Success.")

if __name__ == "__main__":
    test1()
