# N과 M(7)
from sys import stdin
input = stdin.readline

def permutation(start):
    if len(tmp) == M:
        print(' '.join(map(str,tmp)))
        return
    for i in range(len(data)):
        tmp.append(data[i])
        permutation(i)
        tmp.pop() 
     
N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
tmp = []
visited = [0] * N

permutation(0)
