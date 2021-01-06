import sys
sys.stdin = open("1979_whereword.txt", "r")

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    data = []
    result = 0
    count = 0
    for i in range(N):
        line = list(map(int, input().split()))
        data.append(line)

    for y in range(N): #가로 검토
        for x in range(N):
            if count > K:
                count = 0
            elif count == K and (data[y][x]==0):
                result += 1
                count = 0
            if data[y][x] == 1:
                count +=1
            else:
                count = 0
        if count == K:
            result+=1
        count=0

    for x in range(N): #세로 검토
        for y in range(N):
            if count > K:
                count = 0
            elif count == K and (data[y][x]==0):
                result += 1
                count = 0
            if data[y][x] == 1:
                count +=1
            else:
                count=0
        if count == K:
            result+=1
        count=0

    print("#{} {}".format(t,result))