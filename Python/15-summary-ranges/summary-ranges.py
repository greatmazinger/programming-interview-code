from typing import List, Tuple

def getNextRange(nums: List[int]) -> Tuple[str, int]:
    i = 0
    while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
        i += 1
    if i == 0:
        return str(nums[i]), 1
    else:
        return f"{nums[0]}->{nums[i]}", i + 1

def summaryRanges(nums: List[int]) -> List[str]:
    result = []
    i = 0
    length = len(nums)
    while i < length:
        range, num = getNextRange(nums[i:length])
        result.append(range)
        i += num
    return result

def test1():
    print("Running TEST 1:")
    nums = [0,1,2,4,5,7]
    expected = ["0->2", "4->5", "7"]

    result = summaryRanges(nums)
    for i in range(len(result)):
        assert result[i] == expected[i]
    print(" - TEST 1 successful.")


if __name__ == "__main__":
    test1()
