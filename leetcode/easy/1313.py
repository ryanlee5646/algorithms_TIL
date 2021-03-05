# 1313. Decompress Run-Length Encoded List

class Solution(object):
    def decompressRLElist(self, nums):
        result = []
        for i in range(1,len(nums),2):
            result += [nums[i]] * nums[i-1]
        return result