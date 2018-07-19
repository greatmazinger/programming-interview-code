from collections import Counter
from pprint import PrettyPrinter

pp = PrettyPrinter(indent = 4)

class TwoSum(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        imap = {}
        for index in xrange(len(nums)):
            x = nums[index]
            if x not in imap:
                imap[x] = [ index ]
            else:
                imap[x].append(index) 
        counter = Counter(nums)
        counter_orig = Counter(counter)
        for num, count in counter.items():
            want = target - num
            counter_orig[num] -= 1
            if want in counter_orig and counter_orig[want] > 0:
                first = imap[num].pop(0)
                second = imap[want].pop(0)
                if first < second:
                    return [first, second]
                else:
                    return [second, first]
        assert(False)

ts = TwoSum()
nums = [ 0, 3, 4, 0 ]
target = 0
answer = ts.twoSum( nums = nums, target = target )
print "nums:", str(nums)
print "target:", target
pp.pprint(answer)
