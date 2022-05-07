# 드래곤 커브
'''
0: x좌표가 증가하는 방향 (동)
1: y좌표가 감소하는 방향 (북)
2: x좌표가 감소하는 방향 (서)
3: y좌표가 증가하는 방향 (남)

1. 커브는 세대가 증가함에 따라 이전 세대의 커브를 reverse한 값에 +1을 하면됌
2. 커브가 이동함에 따라 해당 좌표를 체크


'''
from sys import stdin
input = stdin.readline

N = int(input())  # 커브의 개수
infos = [list(map(int, input().split())) for _ in range(N)]
data = [[0]*101 for _ in range(101)]
dx = [0, -1, 0, 1]  # 남 서 북 동
dy = [1, 0, -1, 0]

for info in infos:
    y, x, d, g = info
    # 커브 구하기
    curves = [d]
    data[y][x] = 1
    for i in range(g):
        curves += [(j+1) % 4 for j in curves[::-1]]
    # 커브 좌표 찍기
    for curve in curves:
        x += dx[curve]
        y += dy[curve]
        if x < 0 or x >= 101 or y < 0 or y >= 101:
            continue
        data[y][x] = 1

# 정사각형 개수 구하기
result = 0
for y in range(len(data)):
    for x in range(len(data)):
        if data[y][x]:
            if data[y+1][x] and data[y][x+1] and data[y+1][x+1]:
                result += 1
print(result)
