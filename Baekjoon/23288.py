# 주사위 굴리기2
from sys import stdin
input = stdin.readline

# 1. 주사위가 이동 방향으로 한 칸 굴러간다. 
#    이동 방향에 칸이 없다면 반대로 한칸 굴러간다.

# 2. 도착한 칸에(x, y)에 대한 점수를 획득한다

# 3. A(주사위 아랫면)와 B(주사위가 놓인 칸)를 비교해 이동 방향을 결정한다.
#    A > B인 경우 이동 방향을 90도 시계 방향으로 회전
#    A < B인 경우 이동 방향을 90도 반시계 방향으로 회전
#    A = B인 경우 이동 방향에 변화는 없다.  
n, m, move_count = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

print(graph)
