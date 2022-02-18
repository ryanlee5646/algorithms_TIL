# N과 M(8)

# N과 M (6)
from sys import stdin
input = stdin.readline

def combinations(start):
    if len(tmp) == M:
        print(' '.join(map(str, tmp)))
        return

    for i in range(start, len(data)):
        if len(tmp) > 0:
            if tmp[-1] > data[i]:
                continue
        tmp.append(data[i])
        combinations(start+1)
        tmp.pop()

N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
tmp = []
visited = [0] * N
combinations(0)
