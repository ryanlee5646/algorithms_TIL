import sys
sys.stdin = open("cargo_dock.txt", "r")

T = int(input())

for t in range(1,T+1):
    N = int(input())
    time = [[0]*2 for i in range(N)]
    for i in range(N):
        time[i][0], time[i][1] = map(int, input().split())
    time.sort(key=lambda x: x[1])
    count = y =  1
    here = time[0][1]
    while y < N:
        if here <= time[y][0]:
            here = time[y][1]
            y+=1
            count+=1
        else:
            y+=1
    print("#{} {}".format(t,count))
