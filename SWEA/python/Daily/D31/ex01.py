import sys, time
sys.stdin = open("swea_1945.txt","r")
stime = time.time()
def IsSafe(y,x):
    if 0<=y<N and 0<=x<N and not visited[y][x]:
        return True
    else:
        return False
def DFS(y,x,temp):
    global low
    if y == end_y and x == end_x:
        if temp < low:
            low = temp
            return
    if temp >= low:
        return
    for i in range(8):
        new_y = y+dy[i]
        new_x = x+dx[i]
        if IsSafe(new_y,new_x):
            visited[new_y][new_x] = 1
            DFS(new_y,new_x,temp+1)
            visited[new_y][new_x] = 0

dy = [-3, -3, -2, 2, 3, 3, -2, 2]
dx = [-2, 2, -3, -3, -2, 2, 3, 3]
T = int(input())
for t in range(1,T+1):
    N = int(input())
    data = list(map(int, input().split()))
    start_x, start_y = data.pop(0), data.pop(0)
    end_y, end_x = data.pop(0), data.pop(0)
    visited = [[0]*N for _ in range(N)]
    low = 987654321
    DFS(start_y,start_x,0)
    print("#{} {}".format(t, low))
    print(time.time()-stime)