import sys
sys.stdin = open("4881.txt", "r")

def GetSome(y, sofar):
    global N, minsum

    if y == N:
        if sofar < minsum :  #끝까지 다 돌았을 때 sofar가 현재의 최소값보다 더 작으면 sofar가 최소값이 됨
            minsum = sofar
        return

    for x in range(N):
        if not visited[x] and sofar < minsum: # 방문한 적이 없고 sofar가 최소값보다 작으면 아예 거치지 않음
            visited[x] = True
            GetSome(y+1, sofar+MyMap[y][x])
            visited[x] = False # 재귀를 다 돌고나서 이전 단계 방문한 걸 초기화

T = int(input())

for t in range(1, T+1):
    minsum    = 987654321
    N = int(input())
    MyMap = []
    visited = [0] * N
    for i in range(N):
        MyMap.append(list(map(int, input().split())))

    GetSome(0, 0)

    print(f'#{t} {minsum}')



