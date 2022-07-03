# 우주 탐사선
from sys import stdin
input = stdin.readline
INF = int(1e9)


def DFS(start, time, cnt):
    global min_time
    # 다돌기전에 이미 최소값을 넘었으면 리턴(백트래킹)
    if time > min_time:
        return
    if cnt == N:
        min_time = min(min_time, time)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            DFS(i, time + graph[start][i], cnt+1)
            visited[i] = 0  # 끝났으면 초기화


N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
min_time = INF
visited = [0] * N
visited[K] = 1

# 플로이드s 와샬 알고리즘을 사용함으로써(모든 점에서 다른 모든 점으로 가는 최단거리)
for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
# 시작점 행성은 방문한 것으로, 방문해야할 행성수는 N-1
DFS(K, 0, 1)

print(min_time)
