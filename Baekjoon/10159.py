# 저울
'''
비교 결과를 알 수 없는 물건의 개수를 출력
'''
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
            # now는 같은 물건이 아니면서, now > i 보다 크다면 stuff > i인것들 체크
            if now != stuff and graph[stuff][now] == 0:
                graph[stuff][now] = 1
                graph[now][stuff] = -1

            for i in range(1, N+1):
                # now가 i보다 무거우면서 i를 체크한적이 없다면
                if graph[now][i] == 1 and not visited[i]:
                    queue.append(i)


queue = deque()

N = int(input())
M = int(input())
# 행 > 열 좌표로 무거운 물건, 가벼운 물건 체크
graph = [[0]*(N+1) for _ in range(N+1)]  # 숫자 1부터 시작하니까 N+1만큼 만들어줌

for i in range(M):
    heavy, light = map(int, input().split())
    # 무거우면 1 가벼우면 -1로 체크(미리 주어진 관계를 맵에 체크)
    graph[heavy][light] = 1
    graph[light][heavy] = -1
for i in graph:
    print(i)
# 1번 물건부터 탐색
for i in range(1, N+1):
    BFS(i)

for i in range(1, N+1):
    # 자신의 번호를 제외한 물건과의 관계가 0(모르는)개수구하기
    count = 0
    for j in range(1, N+1):
        if j != i and graph[i][j] == 0:
            count += 1
    # print(count)
print("---------------------")
for i in graph:
    print(i)
