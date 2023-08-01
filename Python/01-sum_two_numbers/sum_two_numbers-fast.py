def twoSum(nums: List[int], target: int) -> List[int]:
    looking = {}
    # key = value we are looking for to get target:
    # value = index of other value
    # ie. key + nums[looking[key]] == target
    for index in range(0, len(nums)):
        val = nums[index]
        if val in looking:
            return [index, looking[val]]
        # Not found. Save in looking:
        missing = target - val
        looking[missing] = index
    return []
