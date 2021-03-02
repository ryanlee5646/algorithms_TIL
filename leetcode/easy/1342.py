# 1342. Number of Steps to Reduce a Number to Zero

class Solution(object):
    def numberOfSteps (self, num, steps=0):
        if num == 0:
            return steps

        elif num%2 == 0:
            steps += 1
            return self.numberOfSteps(num // 2, steps)

        elif num%2 != 0:
            num -= 1
            steps += 1
            return self.numberOfSteps(num, steps)