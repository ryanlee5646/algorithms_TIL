# N과 M(1)
from sys import stdin
input = stdin.readline

# 순열 출력값
tmp = []
def permutation():
    if len(tmp) == M:
        print(' '.join(map(str, tmp)))
    
    for i in data:
        if i in tmp:
            continue
        print(i)
        tmp.append(i)
        permutation()
        tmp.pop()    

N, M = map(int, input().split())
data = [i for i in range(1, N+1)]
permutation()
