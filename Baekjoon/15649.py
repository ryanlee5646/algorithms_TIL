# N과 M(1)
from sys import stdin
input = stdin.readline

## 풀이 1 ##
# 순열 출력값
tmp = []
def permutation():
    if len(tmp) == M:
        print(' '.join(map(str, tmp)))
        return
    for i in data:
        if i in tmp:
            continue
        tmp.append(i)
        permutation()
        tmp.pop()    

N, M = map(int, input().split())
data = [i for i in range(1, N+1)]
permutation()

## 풀이 2 ##
# 순열 출력값
def permutation(depth, N, M):
    if len(tmp) == M:
        print(' '.join(map(str, tmp)))
        return
    for i in range(len(data)):
        if not visited[i]:
           visited[i] = 1
           tmp.append(data[i])
           permutation(depth+1, N, M)
           visited[i] = 0 # 끝까지 탐색 했으면 빼주기
           tmp.pop()
 
N, M = map(int, input().split())
data = [i for i in range(1, N+1)]
visited = [0] * N
tmp = []
permutation(0, N, M)

## 풀이3 ##
# itertools이용 permutation 
from itertools import permutations
N, M = map(int, input().split())
data = [i for i in range(1, N+1)]

p = list(permutations(data,M))

for i in p:
    print(' '.join(map(str, i)))