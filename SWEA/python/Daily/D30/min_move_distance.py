import sys
sys.stdin = open("min_move_distance.txt", "r")

def Back(y,x):
    global low, temp
    if x == N:
        if temp < low:
            low = temp
            return
    if temp > low:return
    y = x
    for i in range(N+1):
        if Mymap[y][i] != 0:
            if not visited[i]:
                x = i
                visited[x] = 1
                temp += Mymap[y][i]
                Back(y,x)
                visited[x] = 0
                temp-=Mymap[y][i]

T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split()) #N은 끝점, M 경로 수
    data = [list(map(int,input().split())) for _ in range(M)]
    Mymap = [[0]*(N+1) for _ in range(N)]
    low = 98754321
    temp = 0
    visited = [0] * (N+1)
    for i in range(len(data)):
        Mymap[data[i][0]][data[i][1]] = data[i][2]

    for x in range(N+1):
        if Mymap[0][x] != 0:
            start_y = 0
            start_x = x
            if not visited[start_x]:
                visited[start_x] = 1
                temp += Mymap[start_y][start_x]
                Back(start_y,start_x)
                visited[start_x] = 0
                temp -= Mymap[start_y][start_x]

    print("#{} {}".format(t,low))
from collections import deque

# def BFS(start_y, start_x):
#     queue = deque([(start_y, start_x)])
#     visited[start_y][start_x] = 0
#     while queue:
#         y,x = queue.popleft()
#         y=x
#         for i in range(N+1):
#             if Mymap[y][i] != 0:
#             if # 다음에 갈 위치의 거리보다 현재까지거리 + 다음위치가면서 더해질 거리가 작은가?
#                 visited[ny][nx] = visited[y][x] + Mymap[ny][nx]
#                 Q.append([])
#
#
# T = int(input())
# for t in range(1,T+1):
#     N, M = map(int, input().split()) #N은 끝점, M 경로 수
#     data = [list(map(int,input().split())) for _ in range(M)]
#     print(data)
#     Mymap = [[0]*(N+1) for _ in range(N+1)]
#     low = 98754321
#     temp = 0
#     visited = [987654321] * (N+1)
#     for i in range(len(data)):
#         Mymap[data[i][0]][data[i][1]] = data[i][2]
#     print(Mymap)
#     for x in range(N+1):
#         if Mymap[0][x] != 0:
#             start_y = 0
#             start_x = x
#             BFS(start_y,start_x)
#             break

