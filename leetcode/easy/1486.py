# 1486. XOR Operation in an Array

class Solution(object):
    def xorOperation(self, n, start):
        result = start
        for i in range(1, n):
            result ^= start + 2 * i
        return result



