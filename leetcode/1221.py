# 1221. Split a String in Balanced Strings

class Solution(object):
    def balancedStringSplit(self, s):
        count = 0
        result = 0
        for i in s:
            if i == 'R':
                count += 1
            if i == 'L':
                count -= 1
            if count == 0:
                result += 1
        return result