import sys
sys.stdin = open("square_room.txt", "r")

def IsSafe(y,x,N):
    if 0<=y<N and 0<=x<N :
        return True
    else:
        return False
def DFS(y,x,here):
    for i in range(4):
        newy = y+dy[i]
        newx = x+dx[i]
        if IsSafe(newy,newx,N) and data[newy][newx] == data[y][x] +1:
            if visited[y][x] + 1 > visited[newy][newx]:
                visited[newy][newx] = visited[y][x] + 1
                DFS(newy,newx,here)
                index.append(here + [visited[newy][newx]])
    return
T = int(input())
dy = [1,-1,0,0]
dx = [0,0,1,-1]
for t in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    index = []
    room = []
    result = []
    # print(data)
    # print(visited)
    for y in range(N):
        for x in range(N):
            DFS(y,x,[y,x])
    # print(visited)
    # print(index)
    for i in range(len(index)):
        room.append(index[i][2])
    # print(room)
    for j in index:
        if j[2] == max(room):
            result.append(data[j[0]][j[1]])
    # print(result)
    print("#{} {} {}".format(t,min(result),max(room)+1))
