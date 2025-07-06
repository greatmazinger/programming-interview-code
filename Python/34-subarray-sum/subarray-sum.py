from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # initialize prefixsum
        psum = defaultdict(int)
        psum[0] = 1 # we need this for sums that start at index 0
        cursum = 0
        total = 0
        for i in range(len(nums)):
            cursum += nums[i]
            want = cursum - k
            if want in psum:
                total += psum[want]
            psum[cursum] += 1
        return total
