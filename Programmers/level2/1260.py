# DFS와 BFS
# deque 사용시 기본 queue를 구현하는거 보다 훨씬 빠름
from collections import deque
import sys
read = sys.stdin.readline # input값 빠르게 받기

# 첫번째 정점에서 갈 수있는 곳이 나오면 다음 정점으로 넘어감(재귀호출)
def DFS(start):
    dfs_visit[start] = 1
    print(start, end=" ")
    for i in range(1, N+1):
        if dfs_visit[i] == 0 and data[start][i] == 1:
            DFS(i)
            
# 첫번째 정점에서 갈 수 있는 정점을 모두 큐에 담고 차례로 넘어감    
def BFS(start):
    queue = deque()
    queue.append(start)
    bfs_visit[start] = 1
    while queue:
        start = queue.popleft()
        print(start, end = " ")
        for i in range(1, N+1):
            if bfs_visit[i] == 0 and data[start][i] == 1:
                queue.append(i)
                bfs_visit[i] = 1
    

N, line, start = map(int, read().split())
# 정점이 1부터 시작하므로 N+1로 설정
data = [[0] * (N+1) for _ in range(N+1)] 
# 방문한 정점 체크
dfs_visit = [0] * (N+1) 
bfs_visit = [0] * (N+1)

for _ in range(line):
    x,y = map(int, read().split())
    # 간선 양방향
    data[x][y] = data[y][x] = 1


DFS(start)
print()
BFS(start)

