# 1365. How Many Numbers Are Smaller Than the Current Number

# Solution 1
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        result = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if i != j:
                    if nums[j] < nums[i]:
                        count += 1
            result.append(count)
        return result

# Solution 2(Dictionary)
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        nums1=sorted(list(nums))
        data={}
        result=[]
        for i in range(0,len(nums1)):
            if nums1[i] not in data:
                data[nums1[i]]=i
                val=i
            else:
                data[nums1[i]]=val
        print(data)
        for i in nums:
            if i in data:
                result.append(data[i])
        return result