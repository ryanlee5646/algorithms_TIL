import sys
sys.stdin = open("pipe1.txt","r")

def IsSafe(y,x,N):
    if 0<=y<N and 0<=x<N and data[y][x] != 1:
        return True
    else:
        return False

def DFS(y,x):
    global count, flag
    if y == N-1 and x == N-1:
        count+=1
        return

    if flag == 'garo':
        g_y = [0,1] # 가로, 대각
        g_x = [1,1]
        for i in range(len(g_y)):
            ng_y = y+g_y[i]
            ng_x = x+g_x[i]
            if i == 0:
                flag = 'garo'
                if IsSafe(ng_y,ng_x,N):
                    DFS(ng_y,ng_x)
            else:
                flag = 'cross'
                if IsSafe(ng_y,ng_x,N):
                    if data[ng_y-1][ng_x] != 1 and data[ng_y][ng_x-1] != 1:
                        DFS(ng_y,ng_x)
    elif flag == 'sero':
        s_y = [1,1] # 세로, 대각
        s_x = [0,1]
        for i in range(len(s_y)):
            ns_y = y+s_y[i]
            ns_x = x+s_x[i]
            if i == 0:
                flag = 'sero'
                if IsSafe(ns_y,ns_x,N):
                    DFS(ns_y,ns_x)
            else:
                flag = 'cross'
                if IsSafe(ns_y,ns_x,N):
                    if data[ns_y - 1][ns_x] != 1 and data[ns_y][ns_x - 1] != 1:
                        DFS(ns_y,ns_x)
    elif flag == 'cross':
        c_y = [0,1,1] # 가로, 세로, 대각
        c_x = [1,0,1]
        for i in range(len(c_y)):
            nc_y = y+c_y[i]
            nc_x = x+c_x[i]
            if i == 0:
                flag = 'garo'
                if IsSafe(nc_y,nc_x,N):
                    DFS(nc_y,nc_x)
            elif i == 1:
                flag = 'sero'
                if IsSafe(nc_y,nc_x,N):
                    DFS(nc_y,nc_x)
            else:
                flag = 'cross'
                if IsSafe(nc_y,nc_x,N):
                    if data[nc_y - 1][nc_x] != 1 and data[nc_y][nc_x - 1] != 1:
                        DFS(nc_y,nc_x)

N = int(input())
data = [list(map(int,input().split())) for i in range(N)]
visited = [[0]*N for _ in range(N)]
start_y, start_x = 0, 1
count = 0
flag = 'garo'
DFS(start_y,start_x)
print(count)