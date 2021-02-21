# 1480.  Running Sum of 1d Array
#
class Solution(object):
    def runningSum(self, nums):
        result = []
        for i in range(1,len(nums)+1):
            sum(nums[:i])
            result.append(sum(nums[:i]))
        return result