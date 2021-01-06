import sys
sys.stdin = open("min_cost.txt", "r")

# def Issafe(y,x,N):
#     if y>=0 and y<N and x>=0 and x<N and not visited[y][x]:
#         return True
#     else:
#         return False
# def Back(y,x,temp):
#     global low
#     if y == end_y and x == end_x:
#         if temp < low:
#             low = temp
#             return
#     if low < temp:
#         return
#     for i in range(4):
#         new_y = y+dy[i]
#         new_x = x+dx[i]
#         if Issafe(new_y, new_x, N):
#             visited[new_y][new_x] = 1
#             if data[new_y][new_x] > data[y][x]:
#                 Back(new_y,new_x,temp+(data[new_y][new_x]-data[y][x])+1)
#             else:
#                 Back(y+dy[i],x+dx[i],temp+1)
#             visited[new_y][new_x] = 0
# dy = [1,0,-1,0] #하우상좌
# dx = [0,1,0,-1]
#
# T = int(input())
# for t in range(1,T+1):
#     N = int(input())
#     data = [list(map(int,input().split())) for i in range(N)]
#     low = 987654321
#     visited = [[0]*N for _ in range(N)]
#     end_y = end_x = N-1
#     Back(0,0,0)
#     print("#{} {}".format(t, low))

# def Issafe(y,x,N):
#     if y>=0 and y<N and x>=0 and x<N:
#         return True
#     else:
#         return False
#
# def Back(y,x):
#     global low
#     if y == end_y and x == end_x:
#         low = temp[y][x]
#         return
#
#     for i in range(4):
#         new_y = y + dy[i]
#         new_x = x+dx[i]
#         if Issafe(new_y,new_x,N):
#             if data[y][x] < data[new_y][new_x]:
#                 if temp[y][x] + (data[new_y][new_x] - data[y][x]) +1 < temp[new_y][new_x]:
#                     temp[new_y][new_x] = temp[y][x] + (data[new_y][new_x] - data[y][x]) +1
#                     if temp[new_y][x+dx[i]] > low:
#                         return
#                     else:
#                         Back(new_y, x+dx[i])
#             else:
#                 if temp[y][x] + 1 < temp[new_y][new_x]:
#                     temp[new_y][new_x] = temp[y][x] + 1
#                     if temp[new_y][x+dx[i]] > low:
#                         return
#                     else:
#                         Back(y+dy[i], x+dx[i])
# dy = [1,0,-1,0] #하우상좌
# dx = [0,1,0,-1]
# T = int(input())
# for t in range(1,T+1):
#     N = int(input())
#     data = [list(map(int,input().split())) for i in range(N)]
#     low = 987654321
#     temp = [[987654321]*N for _ in range(N)]
#     temp[0][0] = 0
#     end_y = end_x = N-1
#     Back(0,0)
#     print("#{} {}".format(t, low))

from collections import deque

def Issafe(y,x,N):
    if y>=0 and y<N and x>=0 and x<N:
        return True
    else:
        return False
T = int(input())
for t in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split()))for i in range(N)]
    temp = [[987654321]*N for _ in range(N)]
    temp[0][0] = 0
    queue = deque([(0,0)])
    low = 0
    dy = [1, 0, -1, 0]
    dx = [0,1,0,-1]
    while queue: #큐에 값이 있을때까지 반복
        y, x = queue.popleft()
        for j in range(4):
            new_y = y+dy[j]
            new_x = x+dx[j]
            if Issafe(new_y,new_x,N):
                if data[new_y][new_x] > data[y][x]:
                    if temp[new_y][new_x] > temp[y][x] + (data[new_y][new_x] - data[y][x]) +1:
                        temp[new_y][new_x] = temp[y][x] + (data[new_y][new_x] - data[y][x]) +1
                        queue.append((new_y, new_x))
                else:
                    if temp[new_y][new_x] > temp[y][x] + 1:
                        temp[new_y][new_x] = temp[y][x] + 1
                        queue.append((new_y, new_x))
    low = temp[N-1][N-1]
    print("#{} {}".format(t, low))








