# 이상한 스위치
from collections import deque
import sys

INF = sys.maxsize
input = sys.stdin.readline

N = int(input())

switch = list(map(int, input().split()))

impact = {}
# 영향을 주는 스위치 목록
for i in range(N):
  tmp = list(map(int, input().split()))
  impact[i] = tmp
  

print(switch)
print(impact)
