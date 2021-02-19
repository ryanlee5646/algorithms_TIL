# 1431. Kids With the Greatest Number of Candies

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        max_candies = max(candies)
        for i in candies:
            if (i + extraCandies) < max_candies:
                result.append(False)
            else:
                result.append(True)
        return result