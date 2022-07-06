# 봄버맨
from sys import stdin
input = stdin.readline

N, M, second = map(int, input().split())
graph = [input().rstrip() for _ in range(N)]
time_check = [[0] * M for _ in range(N)]
print(graph)

for y in range(N):
    for x in range(M):
        if graph[y][x] == 'O':
            time_check[y][x] = 1
print(time_check)
