# N과 M (6)
from sys import stdin
input = stdin.readline

def combinations(start):
    if len(tmp) == M:
        print(' '.join(map(str, tmp)))
        return

    for i in range(start, len(data)):
        if not visited[i]:
            visited[i] = 1
            tmp.append(data[i])
            combinations(i+1)
            tmp.pop()
            visited[i] = 0

N, M = map(int, input().split())
data = sorted(list(map(int, input().split())))
tmp = []
visited = [0] * N
combinations(0)
