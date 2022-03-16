# 주사위 굴리기
from sys import stdin
from copy import copy, deepcopy
input = stdin.readline

def roll(course):
    # copy_dice = deepcopy(dice)
    if course == 1: # 동쪽
        dice[0], dice[2], dice[5], dice[1] = dice[2], dice[5], dice[1], dice[0]
    elif course == 2: # 서쪽
        dice[0], dice[1], dice[5], dice[2] = dice[1], dice[5], dice[2], dice[0]
    elif course == 3: # 북쪽
        dice[0], dice[4], dice[5], dice[3] = dice[4], dice[5], dice[3], dice[0]
    else: # 남쪽
        dice[0], dice[3], dice[5], dice[4] = dice[3], dice[5], dice[4], dice[0]
  
    return dice[0]

# def roll_dice(i):
#     global now_y, now_x
#     ny = now_y + dy[i]
#     nx = now_x + dx[i]
#     # 주사위가 맵 범위를 벗어나지 않는다면
#     if 0 <= ny and ny < n  and 0 <= nx and nx < m:
#         # 맵에 칸이 0이라면 주사위 밑면(돌리기전)을 찍어주기
#         roll(i)
#         if graph[ny][nx] == 0:     
#             graph[ny][nx] = dice[5]

#         # 맵에 칸이 0이 아니라면 
#         else:
#             dice[5] = graph[ny][nx]
#             graph[ny][nx] = 0   
#         now_y = ny
#         now_x = nx
#         print(dice[0])
#     return 

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
now_y = x
now_x = y

for i in course:
    ny = now_y + dy[i]
    nx = now_x + dx[i]
    
    # 주사위가 맵 범위를 벗어나면 패스
    if not 0 <= ny < n or not 0 <= nx < m:
        continue
    # 주사위 굴리기
    roll(i)
    # 맵의 칸이 0이라면
    if graph[ny][nx] == 0:     
        graph[ny][nx] = dice[5]

    # 맵에 칸이 0이 아니라면 
    else:
        dice[5] = graph[ny][nx]
        graph[ny][nx] = 0   
    now_y, now_x = ny, nx
    print(dice[0])

