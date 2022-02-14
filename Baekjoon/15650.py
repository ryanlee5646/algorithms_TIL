# N과 M(2) - 조합
from sys import stdin
input = stdin.readline


def combination(start):
    if len(tmp) == M:
        print(' '.join(map(str, tmp)))
        return 
    
    for i in range(start, len(data)):
        if data[i] not in tmp:
            tmp.append(data[i])
            combination(i+1)
            tmp.pop()
            
N, M = map(int, input().split())
data = [i for i in range(1, N+1)]
tmp = []
combination(0)

