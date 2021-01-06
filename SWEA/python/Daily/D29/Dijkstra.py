import sys
sys.stdin = open("Dijkstra.txt", "r")

def dijkstra(start, A, D):
    w = 0
    while V != False:
        temp = 987654321
        for v in V:
            if Mymap[w][v] < temp:
                temp = Mymap[w][v]
                w = v
        V.remove(w)





N = int(input()) #간선 수
Mymap = [[987654321]*6 for _ in range(6)]
V = [i for i in range(1,6)]

for i in range(N):
    y,x = map(int,input().split())
    Mymap[y][x] = int(input())


print(v)





