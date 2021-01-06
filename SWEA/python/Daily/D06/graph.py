import sys
sys.stdin = open('input.txt','r')

MyMap = [[0]*8 for i in range(8)]
visited = [0]*8

def DFS(here):
    print(here)
    visited[here] = True

    for next in range(8):
        if MyMap[here][next] and not visited[next]: #출발지와 도착지 사이 길이 있으면서 방문한적이 없다면
            DFS(next)


Data = list(map(int,input().split()))
howmany = int(len(Data)/2)

for i in range(howmany): # 시작과 끝 지점 좌표에 1을 추가(방향이 안정해져 있기때문에 시작,끝 지점 반대로도 추가)
    Start = Data[i*2]
    Stop = Data[i*2+1]
    MyMap[Start][Stop] = 1
    MyMap[Stop][Start] = 1

DFS(1)
