# N과 M(5)
from itertools import permutations
from sys import stdin
input = stdin.readline

def permutation(start):
    if len(tmp) == M:
        print(' '.join(map(str,tmp)))
        return
    for i in range(len(data)):
        if not visited[i]:
            visited[i] = 1
            tmp.append(data[i])
            permutation(i)
            visited[i] = 0
            tmp.pop() 
     
N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
tmp = []
visited = [0] * N

permutation(0)
