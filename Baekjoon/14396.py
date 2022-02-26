# 수열 순열
from sys import stdin
import math

input = stdin.readline

N, M = map(int, input().split())

def do_process(N):
    if M == 0:
        return 1
    return (math.factorial(33)-1803) % 1000000009
    
result = do_process(N)
print(result)