import sys, time
sys.stdin = open("swea_1945.txt", "r")
stime = time.time()

def Issafe(y,x,N):
    if y>=0 and y<N and x>=0 and x<N and not visited[y][x]:
        return True
    else:
        return False

def Back(y,x,temp):
    global low
    if y == end[0] and x == end[1]:
        if temp < low:
            low = temp
            return
    if temp >= low:
        return

    for i in range(8):
        if Issafe(y+dy[i],x+dx[i],N):
            visited[y][x] = 1
            Back(y+dy[i],x+dx[i],temp+1)
            visited[y][x] = 0
T = int(input())
dy = [2,3,2,-3,-3,-2,3,-2]
dx = [3,2,-3,-2,2,-3,-2,3]

for t in range(1,T+1):
    N = int(input())
    data = list(map(int, input().split()))
    start = [data[1],data[0]]
    end = [data[3], data[2]]
    visited = [[0] * N for _ in range(N)]
    low = 987654321
    Back(start[0], start[1],0)
    print("#{} {}".format(t,low))
    print(time.time()-stime)