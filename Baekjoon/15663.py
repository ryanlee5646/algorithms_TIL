# N과 M(9)
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
            combinations(start+1)
            visited[i] = 0
            tmp.pop() 

N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
tmp = []
visited = [0] * N
combinations(0)