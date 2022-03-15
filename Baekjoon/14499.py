# 주사위 굴리기
from sys import stdin
input = stdin.readline

def roll_dice(course):
    global now_y, now_x
    ny = now_y + dy[course]
    nx = now_x + dx[course]
    # 주사위가 맵 범위를 벗어나지 않는다면
    if ny < n and ny >= 0 and nx < m and nx >= 0:
        # 맵에 칸이 0이라면 주사위 밑면을 찍어주기
        if graph[ny][nx] == 0:
            graph[ny][nx] = dice[course]
        # 맴에 칸이 0이 아니라면 
        else:
            dice[course] = graph[ny][nx]
    
    
    return

n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n) ]

# 동쪽:1, 서쪽:2, 북쪽:3, 남쪽:4
course = list(map(int, input().split()))
# 주사위
dice = [0] * 6
# 방향(동서북남) => 인덱스 1부터 시작
dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, -1, 1]
# 주사위 현재좌표
now_y = y
now_x = x

for i in course:
    roll_dice(i)

