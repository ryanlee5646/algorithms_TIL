import sys
sys.stdin = open("memory_2048.txt", "r")

def combine():
    if dir == 'up':
        for x in range(N):
            for y in range(1,N):
                if data[y-1][x] == data[y][x]:
                    data[y-1][x] *= 2
                    data[y][x] = 0

    if dir == 'down':
        for x in range(N):
            for y in range(N-1,0,-1):
                if data[y-1][x] == data[y][x]:
                    data[y][x] *= 2
                    data[y-1][x] = 0

    elif dir == 'left':
        for y in range(N):
            for x in range(1,N):
                if data[y][x-1] == data[y][x]:
                    data[y][x-1] *= 2
                    data[y][x] = 0
    elif dir == 'right':
        for y in range(N):
            for x in range(N-1,0,-1):
                if data[y][x] == data[y][x-1]:
                    data[y][x] *= 2
                    data[y][x-1] = 0

def push():
    if dir == "up":
        for x in range(N):
            for y in range(0,N-1):
                if data[y][x] == 0:
                    here = y+1
                    while here < N:
                        if data[here][x] != 0:
                            data[y][x], data[here][x] = data[here][x],data[y][x]
                            break
                        else:
                            here+=1
    if dir == "down":
        for x in range(N):
            for y in range(N-1,0,-1):
                if data[y][x] == 0:
                    here = y-1
                    while here > -1:
                        if data[here][x] != 0:
                            data[y][x], data[here][x] = data[here][x],data[y][x]
                            break
                        else:
                            here-=1
    if dir == "left":
        for y in range(N):
            for x in range(0,N-1):
                if data[y][x] == 0:
                    here = x+1
                    while here < N:
                        if data[y][here] != 0:
                            data[y][x], data[y][here] = data[y][here],data[y][x]
                            break
                        else:
                            here+=1
    if dir == "right":
        for y in range(N):
            for x in range(N-1,0,-1):
                if data[y][x] == 0:
                    here = x-1
                    while here > -1:
                        if data[y][here] != 0:
                            data[y][x], data[y][here] = data[y][here],data[y][x]
                            break
                        else:
                            here-=1

T = int(input())
for t in range(1,T+1):
    N, dir = input().split()
    N = int(N)
    data = [list(map(int,input().split())) for _ in range(N)]
    push()
    combine()
    push()
    print("#{}".format(t))
    for i in range(N):
        print(*data[i])