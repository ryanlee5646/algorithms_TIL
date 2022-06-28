# 저울
from sys import stdin
from collections import deque
input = stdin.readline


def BFS(stuff):
    visited = [0] * (N+1)

    queue.append(stuff)

    while queue:
        now = queue.popleft()

        # now 물건을 체크 확인
        if not visited[now]:
            visited[now] = 1
            # now는 같은 물건이 아니면서,
            if now != stuff and graph[stuff][now] == 0:
                graph[stuff][now] = 1
                graph[now][stuff] = -1

            for i in range(1, N+1):
                if graph[now][i] == 1 and not visited[i]:
                    queue.append(i)


queue = deque()

N = int(input())
M = int(input())
# 행 > 열 좌표로 무거운 물건, 가벼운 물건 체크
graph = [[0]*(N+1) for _ in range(N+1)]  # 숫자 1부터 시작하니까 N+1만큼 만들어줌

for i in range(M):
    heavy, light = map(int, input().split())
    # 무거우면 1 가벼우면 -1로 체크
    graph[heavy][light] = 1
    graph[light][heavy] = -1

# 1번 물건부터 탐색
for i in range(1, N+1):
    BFS(i)

for i in range(1, N+1):
    # 번호가 같은 물건 말고
    count = 0
    for j in range(1, N+1):
        if j != i and graph[i][j] == 0:
            count += 1
    print(count)

for i in graph:
    print(i)
