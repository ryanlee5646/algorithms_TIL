import sys
sys.stdin = open("4875_미로.txt", "r")

def IsSafe(y,x,N):
    if x>=0 and x<N and y>=0 and y<N and data[y][x] != 1:  #범위를 벗어나면 안되는 조건과 벽은 지나가지 않는 조건
        return True
    else:
        return False


def DFS(Start_y, Start_x):

    data[Start_y][Start_x] = 1
    if data[y][x] == 3:
        return
    else:
        for i in range(4):
            if IsSafe(Start_y+dy[i],Start_x+dx[i], N):
                    DFS(Start_y+dy[i], Start_x+dx[i])

T = int(input())
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for t in range(1, T+1):
    N = int(input())
    data = []
    for i in range(N): # 데이터 생성
        data.append(list(map(int, input())))
    for y in range(N):
        for x in range(N):
            if data[y][x] == 2: # 2를 찾을경우 시작지점
                Start_y = y
                Start_x = x
            elif data[y][x] == 3: # 3을 찾을 경우 끝 지점
                End_y = y
                End_x = x
    DFS(Start_y, Start_x)

    if data[End_y][End_x] == 1:
        print(f"#{t} 1")
    else:
        print(f"#{t} 0")

