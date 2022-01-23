# DFS와 BFS
from collections import deque
import sys
read = sys.stdin.readlines

N, line, start = map(int, read().split())

data = [[0] * (N+1) for _ in range(N+1)]

dfs_visit = [0] * (N+1) 
bfs_visit = [0] * (N+1)

for _ in range(line):
    x,y = map(int, read().split())
    data[x][y] = data[y][x] = 1

print(data)