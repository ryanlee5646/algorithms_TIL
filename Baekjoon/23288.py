# 주사위 굴리기2
from sys import stdin
input = stdin.readline

n, m, move_count = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

print(graph)
