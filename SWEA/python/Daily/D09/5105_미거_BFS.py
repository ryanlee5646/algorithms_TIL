import sys

sys.stdin = open("4875_미로.txt", "r")


def IsSafe(y, x, N):
    if x >= 0 and x < N and y >= 0 and y < N and data[y][x] != 1:
        return True
    else:
        return False


def BFS(Start_y, Start_x):
    global count
    queue = []

    queue.append([Start_y, Start_x])

    while queue:
        y, x = queue.pop(0)
        for dir in range(4):
            new_y = y + dy[dir]
            new_x = x + dx[dir]
            if IsSafe(new_y, new_x, N):
                if data[new_y][new_x] != 1:
                    data[new_y][new_x] = 1
                    queue.append([new_y, new_x])
                    distance[new_y][new_x] = distance[y][x] + 1


T = int(input())
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
for t in range(1, T + 1):
    N = int(input())
    data = []
    distance = []
    for i in range(N):
        distance.append([0]*N)
    print(distance)

    for i in range(N):
        data.append(list(map(int, input())))
    for y in range(N):
        for x in range(N):
            if data[y][x] == 2:
                Start_y = y
                Start_x = x
            elif data[y][x] == 3:
                End_y = y
                End_x = x
    BFS(Start_y, Start_x)

    if data[End_y][End_x] == 1:
        print(f"#{t} {distance[End_y][End_x]-1}")  # 마지막에 3을만나면 한칸 더 올라감
    else:
        print(f"#{t} 0")
