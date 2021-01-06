import sys
sys.stdin = open("junhyeok.txt", "r")



def Junhyeok(y, cost):
    global cost_sum, n, Flag

    if y == n:
        Flag = True
        if cost < cost_sum : #cost = 누적된 비용 , cost_sum = 최소비용
            cost_sum = cost
        return

    for x in range(1,n+1):
        if not visited[x] and cost < cost_sum and Costs[y][x] != 0: #방문한적 없으면서 누적 비용이 최소비용보다 작으면서 Costs좌표에 값이 있으면 실행
            visited[x] = True
            Junhyeok(x, cost+Costs[y][x])
            visited[x] = False

Flag = False
cost_sum = 98765432
n, m = map(int, input().split())
Costs = [[0]*(n+1) for i in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    y, x, Cost = map(int, input().split())
    Costs[y][x] = Cost

Junhyeok(1,0)
if Flag == False:
    print(-1)
else:
    print(cost_sum)