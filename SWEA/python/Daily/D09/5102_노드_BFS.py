import sys
sys.stdin = open("5102_노드_BFS.txt", "r")

T = int(input())


def BFS(start):
    global V
    queue = []
    visited[start] = 1
    queue.append(start) #시작지점을 visited에 찍어줌

    while queue:
        here = queue.pop(0)

        for next in range(1, V+1):
            if visited[next] != 1 and Mymap[here][next] == 1 :
                visited[next] = 1
                queue.append(next)
                distance[next] = distance[here] +1
                print(distance)


for t in range(1,T+1):
    V, E = map(int,input().split())
    distance = [0] * (V+1)
    visited = [0] * (V+1)
    Mymap = [[0] * (V+1) for i in range(V+1)]
    node = []

    for i in range(E):
        node.append(list(map(int, input().split())))
        Mymap[node[i][0]][node[i][1]] = 1  #값을 넣어줌
        Mymap[node[i][1]][node[i][0]] = 1
    start, end = map(int, input().split())
    BFS(start)
    print(f"#{t} {distance[end]}")