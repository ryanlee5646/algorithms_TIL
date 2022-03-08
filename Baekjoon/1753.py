# 최단경로
from sys import stdin
input = stdin.readline

def Dijkstra(start):
    
    return
    

# 노드수, 간선수
N, M = map(int, input().split())
start = int(input())
data = [[] for _ in range(N+1)]
distance = [int(1e9)] * (N+1)
visited = [0] * (N+1)

for i in range(M):
    s, e, w = map(int, input().split())
    data[s].append((e,w))


Dijkstra(start)
