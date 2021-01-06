import sys
sys.stdin = open("minsum_5188.txt", "r")

def IsSafe(y,x,N):
    if x>=0 and x<N and y>=0 and y<N:
        return True
    else:
        return False

def DFS(y,x):
    global temp, min_num, end_y, end_x
    if y == end_y and x == end_x:
        if min_num >= temp:
            min_num = temp
        return
    if min_num < temp:
        return

    for i in range(2):
        if IsSafe(y+dy[i],x+dx[i],N):
            temp+= data[y+dy[i]][x+dx[i]]
            DFS(y+dy[i],x+dx[i])
            temp -= data[y+dy[i]][x+dx[i]]

T = int(input())
dy = [1,0] #아래
dx = [0,1] #오른쪽

for t in range(1, T+1):
    N = int(input()) # 맵 크기
    data = []
    for i in range(N):
        data.append(list(map(int, input().split())))
    temp = data[0][0]
    min_num = 123124354
    end_y,end_x = N-1, N-1
    DFS(0,0)
    print("#{} {}".format(t,min_num))