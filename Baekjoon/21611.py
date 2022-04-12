# 마법사 상어와 블리자드
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
blizards = [list(map(int, input().split())) for _ in range(m)]
dx = [0, 0, -1, 1] # 위 아래 좌 우
dy = [-1, 1, 0, 0]
print()
for i in graph:
    print(*i)
print()
print(blizards)

