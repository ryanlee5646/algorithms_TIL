# 바지구매
from sys import stdin
input = stdin.readline

a, b, c, d = map(int, input().split())
N = int(input())
count = 0
for i in range(N):
  # 둘레, 바지길이
  circle, x = map(int, input().split())
  result = max(a*(((x-b)**2))+c, d)
  
  if result == circle: # 둘레가 같으면 count +1
    count += 1
    
print(count)

  