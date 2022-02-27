# 연구소1
from collections import deque
from copy import deepcopy
from sys import stdin

input = stdin.readline

# 바이러스 퍼트리기
def BFS():
    global safe_zone
    # 조합을 구하기 위한 데이터맵과 섞이면 안되니까 깊은 복사 해줌 
    copy_data = deepcopy(data)
    queue = deque()
    for y in range(N):
        for x in range(M):
            # 바이러스 위치 큐에 추가
            if copy_data[y][x] == 2:
                queue.append((y, x))

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            _x = x + dx[i]
            _y = y + dy[i]
            if _x >= 0 and _y >= 0 and _x < M and _y < N:
                if copy_data[_y][_x] == 0:
                    copy_data[_y][_x] = 2
                    queue.append((_y, _x))
    tmp = 0
    for i in copy_data:
        tmp += i.count(0)
                 
    if tmp > safe_zone:
        safe_zone = tmp

# 3개 기둥 조합 구하기
def three_walls(depth):
    if depth == 3:
        BFS()
        return
    for y in range(N):
        for x in range(M):
            if data[y][x] == 0:
                data[y][x] = 1
                three_walls(depth+1)
                data[y][x] = 0

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
# 탐색방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# 안전영역 갯수
safe_zone = 0
three_walls(0)

print(safe_zone)