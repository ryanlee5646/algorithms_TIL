# N과 M (3) -순열(중복 숫자 인정)
from sys import stdin
input = stdin.readline
def permutation(depth):
    if len(tmp) == M:
        print(' '.join(map(str, tmp)))
        return
    for i in range(len(data)):
        # if not visited[i]:
        # 중복 체크 안하면됌
        #    visited[i] = 1
        tmp.append(data[i])
        permutation(depth+1)
        #    visited[i] = 0 # 끝까지 탐색 했으면 빼
        tmp.pop()
 
N, M = map(int, input().split())
data = [i for i in range(1, N+1)]
visited = [0] * N
tmp = []
permutation(0)