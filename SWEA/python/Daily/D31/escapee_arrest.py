import sys, time
sys.stdin = open("escapee_arrest.txt", "r")
stime = time.time()
# issafe 를 파이프 별로 만들어주자
# DFS

# dy = {1:[-1,1,0,0], #상하좌우
#       2:[-1,1,0,0], #상하
#       3:[0,0,0,0], #좌우
#       4:[-1,0,0,0], #상우
#       5:[1,0,0,0], #하우
#       6:[1,0,0,0], #하좌
#       7:[-1,0,0,0]
#       } #상좌
# dx = {1:[0,0,-1,1], #상하좌우
#       2:[0,0,0,0], #상하
#       3:[-1,1,0,0], #좌우
#       4:[0,1,0,0], #상우
#       5:[0,1,0,0], #하우
#       6:[0,-1,0,0], #하좌
#       7:[0,-1,0,0]
#       } #상좌
#
# def IsSafe(y,x,N,M):
#     if  0<=y<N and 0<=x<M:
#         return True
#     else:
#         return False
# def Back(y,x,time1):
#     if time1 == 0:
#         return
#     visited[y][x]=time1
#     pipe_num = data[y][x]
#     for i in range(4):
#         newy= y+dy[pipe_num][i]
#         newx= x+dx[pipe_num][i]
#         if dy[pipe_num][i] == -1 and IsSafe(newy,newx,N,M):
#             if data[newy][newx] in [1,2,5,6]:
#                 if visited[newy][newx] < time1:
#                     Back(newy,newx,time1-1)
#
#         elif dy[pipe_num][i] == 1 and IsSafe(newy,newx,N,M):
#             if data[newy][newx] in [1,2,4,7]:
#                 if visited[newy][newx] < time1:
#                     Back(newy,newx,time1-1)
#
#         elif dx[pipe_num][i] == -1 and IsSafe(newy, newx, N, M):
#             if data[newy][newx] in [1,3,4,5]:
#                 if visited[newy][newx] < time1:
#                     Back(newy,newx,time1-1)
#
#         elif dx[pipe_num][i] == 1 and IsSafe(newy,newx,N,M):
#             if data[newy][newx] in [1,3,6,7]:
#                 if visited[newy][newx] < time1:
#                     Back(newy,newx,time1-1)
#
# T = int(input())
# for t in range(1,T+1):
#     N, M, sy, sx, time1 = map(int, input().split())
#     data = []
#     start_y = sy
#     start_x = sx
#     visited = [[0]*M for _ in range(N)]
#     count = 0
#     for i in range(N):
#         data.append(list(map(int,input().split())))
#     Back(start_y,start_x,time1)
#     for y in range(N):
#         for x in range(M):
#             if visited[y][x] != 0:
#                 count+=1
#     print("#{} {}".format(t,count))
#     print(time.time() - stime)

#BFS

dy = {1: [-1, 1, 0, 0],  # 상하좌우
      2: [-1, 1, 0, 0],  # 상하
      3: [0, 0, 0, 0],  # 좌우
      4: [-1, 0, 0, 0],  # 상우
      5: [1, 0, 0, 0],  # 하우
      6: [1, 0, 0, 0],  # 하좌
      7: [-1, 0, 0, 0]
      }  # 상좌
dx = {1: [0, 0, -1, 1],  # 상하좌우
      2: [0, 0, 0, 0],  # 상하
      3: [-1, 1, 0, 0],  # 좌우
      4: [0, 1, 0, 0],  # 상우
      5: [0, 1, 0, 0],  # 하우
      6: [0, -1, 0, 0],  # 하좌
      7: [0, -1, 0, 0]
      }  # 상좌
def IsSafe(y,x,N,M):
    if  0<=y<N and 0<=x<M and not visited[y][x]:
        return True
    else:
        return False
def BFS(start_y,start_x,time1):
    visited[start_y][start_x] = 1
    queue = [(start_y,start_x)]
    while queue :
        y, x = queue.pop(0)
        if visited[y][x] == time1:
            break
        pipe_num = data[y][x]
        for i in range(4):
            newy= y+dy[pipe_num][i]
            newx= x+dx[pipe_num][i]
            if dy[pipe_num][i] == -1 and IsSafe(newy,newx,N,M):
                if data[newy][newx] in [1,2,5,6]:
                    visited[newy][newx] = visited[y][x]+1
                    queue.append((newy,newx))

            elif dy[pipe_num][i] == 1 and IsSafe(newy,newx,N,M):
                if data[newy][newx] in [1,2,4,7]:
                    visited[newy][newx] = visited[y][x] + 1
                    queue.append((newy, newx))

            elif dx[pipe_num][i] == -1 and IsSafe(newy, newx, N, M):
                if data[newy][newx] in [1,3,4,5]:
                    visited[newy][newx] = visited[y][x] + 1
                    queue.append((newy, newx))

            elif dx[pipe_num][i] == 1 and IsSafe(newy,newx,N,M):
                if data[newy][newx] in [1,3,6,7]:
                    visited[newy][newx] = visited[y][x] + 1
                    queue.append((newy, newx))
T = int(input())
for t in range(1,T+1):
    N, M, sy, sx, time1 = map(int, input().split())
    data = []
    start_y = sy
    start_x = sx
    visited = [[0]*M for _ in range(N)]
    count = 0
    for i in range(N):
        data.append(list(map(int,input().split())))

    BFS(start_y,start_x,time1)
    for y in range(N):
        for x in range(M):
            if visited[y][x] != 0:
                count+=1

    print("#{} {}".format(t,count))
    print(time.time() - stime)




