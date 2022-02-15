# N과 M(1) - 순열
from sys import stdin
input = stdin.readline

## 풀이 1 ##
# def permutation():
#     if len(tmp) == M:
#         print(' '.join(map(str, tmp)))
#         return
#     for i in data:
#         if i in tmp:
#             continue
#         tmp.append(i)
#         permutation()
#         tmp.pop()    

# N, M = map(int, input().split())
# data = [i for i in range(1, N+1)]
# # 순열 출력값
# tmp = []
# permutation()

## 풀이 2 ##

def permutation(depth):
    if len(tmp) == M:
        print(' '.join(map(str, tmp)))
        return
    for i in range(len(data)):
        if not visited[i]:
           visited[i] = 1
           tmp.append(data[i])
           permutation(depth+1)
           visited[i] = 0 # 끝까지 탐색 했으면 빼
           tmp.pop()
 
N, M = map(int, input().split())
data = [i for i in range(1, N+1)]
visited = [0] * N
tmp = []
permutation(0)

## 풀이3 ##
# itertools이용 permutation 
# from itertools import permutations
# N, M = map(int, input().split())
# data = [i for i in range(1, N+1)]

# p = list(permutations(data,M))

# for i in p:
#     print(' '.join(map(str, i)))