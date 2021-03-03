# 1281. Subtract the Product and Sum of Digits of an Integer

class Solution(object):
    def subtractProductAndSum(self, n):
        sum_num = 0
        digit_num = 1
        for i in str(n):
            sum_num += int(i)
            digit_num *= int(i)

        return digit_num - sum_num

