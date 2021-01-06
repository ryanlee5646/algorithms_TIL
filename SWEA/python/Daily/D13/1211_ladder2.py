import sys
sys.stdin = open("1211_ladder2.txt", "r")

def IsSafe(y,x,N):
    if y>=0 and y<N and x>=0 and x<N and visited[y][x] != 1 and ladder[y][x] ==1: # 범위넘지 않고, 방문한적 없고, 길이 있는 경우
        return True
    else:
        return False

def DFS(y,x):
    global move
    visited[y][x] = 1
    for dir in range(3):
        if IsSafe(y+dy[dir],x+dx[dir], 100) :
            DFS(y+dy[dir],x+dx[dir])
            move+=1
            move_list.append(move)


dy = [0, 0, 1]
dx = [-1, 1, 0]

for t in range(1):
    T = int(input())
    ladder = []
    start = []
    move_list = []
    move = 0
    visited = [[0]*100 for _ in range(100)]
    for i in range(100):
        ladder.append(list(map(int,input().split())))
    print(ladder)


    for x in range(100): #시작지점
        if ladder[0][x] == 1 and visited[0][x] == 0:
            start_y = 0
            start_x = x
            start.append(start_x)
            move=0
            DFS(start_y, start_x)
    print(start)
    print(move)
    print(move_list)