# 입국심사
from sys import stdin
input = stdin.readline


# N:입국심사대 / M:사람 수
N, M = map(int, input().split())
times = []

for i in range(N):
  times.append(int(input()))

times.sort() # 이진

result = 0
left = min(times) 
right = max(times)*M

while left <= right:
  mid = (left+right) // 2 
  people = 0
  
  for time in times:
    people += mid // time # mid시간 동안 심사대별 최대 몇명이 통과할 수 있는지 구함
  
  if people >= M: # 총 통과 해야하는 인원(M)보다 mid 시간에 통과한 인원(people) 수가 많을 경우
    result = mid 
    right= mid - 1 # 더 적은 시간 쪽으로 이분
    
  elif people < M: # 총 통과 해야하는 인원(M)보다 mid 시간에 통과한 인원(people) 수가 적을 경우
    left = mid + 1 # 더 많은 시간을 쪽으로 이분

print(result)