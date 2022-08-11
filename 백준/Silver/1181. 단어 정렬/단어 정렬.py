# 단어정렬
from sys import stdin
input = stdin.readline

N = int(input())

data = [input().rstrip() for i in range(N)]

# 중복제거
data = list(set(data))

# 사전 순으로 정렬
data.sort()

# 길이순으로 정렬
data.sort(key=len)

for i in range(len(data)):
  print(data[i])