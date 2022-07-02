# 저울
from sys import stdin
from collections import deque
input = stdin.readline

q = deque()


def BFS(target):
    global N, H
    visited = [False]*(N+1)

    q.append(target)
    while q:
        now = q.popleft()

        # now가 방문을 아직 안했는가?
        if not visited[now]:
            visited[now] = True
            # now는 target이 아니면서, H[target][now]가 0인가?
            if now != target and H[target][now] == 0:
                H[target][now] = 1
                H[now][target] = -1

            # H[now][i]가 1인 노드를 넣는다.
            for i in range(1, N+1):
                # 아직 i는 방문을 안한상태
                if (H[now][i] == 1) and (not visited[i]):
                    q.append(i)


N = int(input())
M = int(input())
H = [[0]*(N+1) for _ in range(N+1)]

# 미리 측정된 물건 쌍 (앞물건>뒤물건)
for _ in range(M):
    heavy, light = map(int, input().strip().split())
    H[heavy][light] = 1  # heavy>light
    H[light][heavy] = -1  # light<heavy

# 1번부터 탐색
for target in range(1, N+1):
    BFS(target)


# 탐색한 결과, 물건i(1~N)과 비교결과를 알 수 없는 물건의 개수를 출력
for i in range(1, N+1):
    # 자기자신을 제외한 나머지
    cnt = 0
    for j in range(1, N+1):
        if j != i and H[i][j] == 0:
            cnt += 1
    print(cnt)
