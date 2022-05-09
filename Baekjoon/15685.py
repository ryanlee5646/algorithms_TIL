# 드래곤 커브
'''
0: x좌표가 증가하는 방향 (동) 
1: y좌표가 감소하는 방향 (북)
2: x좌표가 감소하는 방향 (서)
3: y좌표가 증가하는 방향 (남)

1. 커브는 세대가 증가함에 따라 이전 세대의 커브를 reverse한 값에 +1을 하면됌
2. 커브가 이동함에 따라 해당 좌표를 체크
3. 좌표값을 기준으로 정사각형 꼭지점 위치가 모두 드래곤 커브 좌표인지 확인(Y:X, Y+1:X, Y:X+1, Y+1:X+1)

'''
from sys import stdin
input = stdin.readline

N = int(input())  # 커브의 개수
infos = [list(map(int, input().split())) for _ in range(N)]
data = [[0]*101 for _ in range(101)]

dx = [1, 0, -1, 0]  # 동 북 서 남
dy = [0, -1, 0, 1]

for info in infos:
    x, y, d, g = info
    # 커브 구하기
    curves = [d]
    data[y][x] = 1
    for i in range(g):
        curves += [(j+1) % 4 for j in curves[::-1]]
    # 커브 좌표 찍기
    for curve in curves:
        x += dx[curve]
        y += dy[curve]
        # if 0 <= x <= 100 and 0 <= y <= 100:
        data[y][x] = 1

# 정사각형 개수 구하기
result = 0
for y in range(100):
    for x in range(100):
        if data[y][x]:
            if data[y+1][x] and data[y][x+1] and data[y+1][x+1]:
                result += 1
print(result)
