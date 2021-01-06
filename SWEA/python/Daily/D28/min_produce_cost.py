import sys
sys.stdin = open("min_produce_cost.txt", "r")


def Back(y, temp):
    global min_cost
    if y == N:
        if temp <= min_cost:
            min_cost = temp
    if temp > min_cost:
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            Back(y+1, temp+data[y][i])
            visited[i] = 0

T = int(input())
for t in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for i in range(N)]
    print(data)
    visited = [0] * N
    min_cost = 987654321
    Back(0,0)
    print("#{} {}".format(t, min_cost))

