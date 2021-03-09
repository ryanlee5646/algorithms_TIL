# 1389. Create Target Array in the Given Order

class Solution(object):
    def createTargetArray(self, nums, index):
        result = []
        for i in range(len(nums)):
            result.insert(index[i], nums[i])
        return result



class Solution(object):
    def createTargetArray(self, nums, index):
        res = []
        for i, idx in enumerate(index):
            res.insert(idx, nums[i])
        return res