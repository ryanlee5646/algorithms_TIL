import sys
sys.stdin = open("problem2.txt", "r")

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def IsSafe(y,x,N):
    if y>=0 and y<N and x>=0 and x<N and Sum_map[y][x] != 0:
        return True
    else:
        return False


def DFS(y, x):
    height.append(Sum_map[y][x])
    visited[y][x] = 1
    for dir in range(4):
        if IsSafe(y+dy[dir], x+dx[dir], N) and not visited[y+dy[dir]][x+dx[dir]]:
            DFS(y+dy[dir], x+dx[dir])

T = int(input())
for t in range(1,T+1):
    N = int(input())
    visited = [[0] * N for _ in range(N)]
    Sum_map = []
    Sum_num = 0
    height = []
    for i in range(N):
        Sum_map.append(list(map(int, input().split())))

    for y in range(N):
        for x in range(N):
            if Sum_map[y][x] > 0 and visited[y][x] == 0:
                start_y = y
                start_x = x
                Sum_num += 1
                DFS(start_y,start_x)

    print("#{} {} {}".format(t,Sum_num,max(height)))














