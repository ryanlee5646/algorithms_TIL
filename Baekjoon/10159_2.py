# 저울
'''
비교 결과를 알 수 없는 물건의 개수를 출력
'''
from sys import stdin
input = stdin.readline

N = int(input())
M = int(input())
# 행 > 열 좌표로 무거운 물건, 가벼운 물건 체크
graph = [[0]*(N+1) for _ in range(N+1)]  # 숫자 1부터 시작하니까 N+1만큼 만들어줌

for i in range(M):
    start, end = map(int, input().split())
    # 무거우면 1 가벼우면 -1로 체크(미리 주어진 관계를 맵에 체크)
    graph[start-1][end-1] = 1

for m in range(N):
    for s in range(N):
        for e in range(N):
            if graph[s][m] and graph[m][e]:
                graph[s][e] = 1

for i in range(N):
    count = 0
    for j in range(N):
        if i == j:
            continue
        if not graph[i][j] and not graph[j][i]:
            count += 1
    print(count)
