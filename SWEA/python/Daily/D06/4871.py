import sys
sys.stdin = open("4871.txt", "r")

T = int(input())

def DFS(here):
    visited[here] = 1
    for next in range(50):
        if Node[here][next] and not visited[next]:
            DFS(next)

for t in range(T):
    Node = [[0] * 50 for i in range(50)]
    visited = [0] * 50
    V, E = map(int, input().split())  # V: 노드 개수 E: E개만큼 간선 수
    for i in range(E): # 간선 수 만큼 반복 입력 받은 데이터 값을  즉시 Node 맵에 넣어줌
        Data = list(map(int,input().split()))
        Start = Data[0]
        Goal = Data[1]
        Node[Start][Goal] = 1
    S, G = map(int, input().split())  #S: 출발 G:도착
    DFS(S)
    if visited[G] == 1:
        print(f'#{t+1} {visited[G]}')
    else:
        print(f'#{t+1} {visited[G]}')




