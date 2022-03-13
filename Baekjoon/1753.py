# 최단경로
from sys import stdin
input = stdin.readline
INF = int(1e9)

def dijkstra(start):
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = 0
    for i in graph[start]:
        distance[i[0]] = i[1]
        
    # 시작 노드를 제외한 전체 N-1개의 노드에 대해 반복
    for i in range(N-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문철
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost
    
# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단거리가 짧은 노드(인덱스)
    for i in range(1, N+1): 
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index
    
# 노드수, 간선수
N, M = map(int, input().split())
start = int(input())
graph = [[] for _ in range(N+1)]
# 최단거리 테이블 모두 무한으로 초기화
distance = [INF] * (N+1)
# 노드방문 체크
visited = [0] * (N+1)

for i in range(M):
    s, e, w = map(int, input().split())
    # s(시작)에서 e(끝점)으로 가는 w(가중치)
    graph[s].append((e,w))

dijkstra(start)

for i in range(1, N+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])