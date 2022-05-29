# 1. 소수만들기

import math
from itertools import combinations 
def prime_num(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    combi = list(combinations(nums, 3))
    for i in combi:
      if prime_num(sum(i)):
        answer+=1
    return answer

result = solution([1,2,3,4])
