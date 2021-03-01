# 1512. Number of Good Pairs

class Solution(object):
    # def numIdenticalPairs(self, nums):
    #     count = 0
    #     for i in range(len(nums)):
    #         for j in range(len(nums)):
    #             if nums[i] == nums[j]:
    #                 if i < j:
    #                     count += 1
    #     return count

    def numIdenticalPairs(self, nums):
        count = 0
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if i < j:
                    if nums[i] == nums[j]:
                        count += 1
        return count