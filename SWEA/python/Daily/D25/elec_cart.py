import sys
sys.stdin = open("elec_cart.txt", "r")

def DFS(here):
    global temp, min_use
    if 0 not in visited: # 종료조건(모든 visited가 1이면 종료)
        temp += data[here][0] #종료하기전에 temp에 마지막 도착점 추가
        if min_use >= temp: # 현재의 최소값보다 더해진값이 더 작다면 초기화
            min_use = temp
        temp-=data[here][0]
        return

    if min_use < temp: #더해지고 있는 값이 최소값보다 크면 리턴
        return

    for i in range(1,N):
        if not visited[i]:
            visited[i] = 1
            next = i
            temp += data[here][next]
            DFS(next)
            visited[i] = 0
            temp -= data[here][next]

T= int(input())
for t in range(1, T+1):
    N = int(input())
    data = []
    visited = [0]*N
    visited[0]=1 # visited 0번째는 방문할걸로 초기화
    temp = 0 # 계속 더해지는 사용량
    min_use = 21442336 #
    for i in range(N):
        data.append(list(map(int,input().split())))

    DFS(0)
    print("#{} {}".format(t,min_use))
