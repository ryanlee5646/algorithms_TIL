import sys
sys.stdin = open('dessert.txt','r')

def IsSafe(y,x):
    if 0<=y<N and 0<=x<N and visited[data[y][x]] != 1:
        return True
    else:
        return False

def DFS(y, x, count, dir):
    global result
    if y == sy and x == sx and dir == 3 :
        if count > result:
            result = count
            return
    ny = y + dy[dir]
    nx = x + dx[dir]
    if IsSafe(ny, nx):
        visited[data[ny][nx]] = 1
        DFS(ny,nx,count+1,dir)
        visited[data[ny][nx]] = 0

    if dir<3 and IsSafe(y+dy[dir+1], x+dx[dir+1]):
        visited[data[y+dy[dir+1]][x+dx[dir+1]]] = 1
        DFS(y+dy[dir+1],x+dx[dir+1],count+1,dir+1)
        visited[data[y+dy[dir+1]][x+dx[dir+1]]] = 0


dy = [1, 1,-1,-1] # 하, 하, 상, 상
dx = [-1, 1,1,-1] # 좌, 우, 우, 좌

T = int(input())
for t in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    visited = [0] * 101
    result = 0
    for sy in range(N):
        for sx in range(N):
            DFS(sy,sx,0, 0)

    if result < 4:
        print("#{} -1".format(t))
    else:
        print("#{} {}".format(t, result))