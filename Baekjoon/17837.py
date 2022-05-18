# 새로운 게임2
from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
chess_infos = [list(map(int, input().split())) for _ in range(k)]
dx = [0, 0 , -1, 1]
dy = [-1, 1, 0, 0]

print(graph)
print(chess_infos)
