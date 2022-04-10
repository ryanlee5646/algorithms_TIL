# 주사위 굴리기2
from sys import stdin
from collections import deque
input = stdin.readline

# 굴리기
def roll(direction):
    if direction == 1: # 동쪽
        dice[0], dice[2], dice[5], dice[3] = dice[3], dice[0], dice[2], dice[5]
    elif direction == 2: # 서쪽
        dice[0], dice[2], dice[5], dice[3] = dice[2], dice[5], dice[3], dice[0]
    elif direction == 3: # 남쪽
        dice[0], dice[1], dice[5], dice[4] = dice[1], dice[5], dice[4], dice[0]
    else: # 북쪽
        dice[0], dice[1], dice[5], dice[4] = dice[4], dice[0], dice[1], dice[5]

# 다음방향 결졍
def next_direction(direction, ny, nx):
    if dice[5] > graph[ny][nx]:
        if direction == 1: # 동 -> 남
            direction = 3
        elif direction == 3: # 남 -> 서
            direction = 2
        elif direction == 2: # 서 -> 북
            direction = 4
        else:   # 북 -> 동
            direction = 1    
    elif dice[5] < graph[ny][nx]:
        if direction == 1: # 동 -> 북
            direction = 4
        elif direction == 4: # 북 -> 서
            direction = 2
        elif direction == 2: # 서 -> 남
            direction = 3
        else: # 남 -> 동
            direction = 1  
    return direction


def get_score(nx, ny):
    queue = deque()
    visited = [[0] * m for _ in range(n)]
    queue.append((ny, nx))
    visited[ny][nx] = 1
    cnt = 0
    while queue:
        y, x = queue.popleft()
        for i in range(1, 5):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if not 0 <= next_x < m and 0 <= next_y < n:
                continue
            if not visited[next_y][next_x] and graph[next_y][next_x] == graph[ny][nx]:
                cnt+=1
                visited[next_y][next_x] = 1
                queue.append((next_y, next_x))
    return cnt    
    
def roll_dice(start_x, start_y, move_count, direction):
    global score
    if move_count == 0:
        return
    
    # 이동할 방향
    nx = start_x + dx[direction]
    ny = start_y + dy[direction] 
    
    if not 0 <= nx < m and 0 <= ny < n:
        if direction == 1: # 동 -> 서
            nx = start_x + dx[2]
            ny = start_y + dy[2]
        elif direction == 2: # 서 -> 동
            nx = start_x + dx[1]
            ny = start_y + dy[1]
        elif direction == 3: # 남 -> 북
            nx = start_x + dx[4]
            ny = start_y + dy[4]
        else: # 북 -> 남
            nx = start_x + dx[3]
            ny = start_y + dy[3]
    # 이동한 칸의 점수 획득
    score += graph[ny][nx]
    # 주사위 굴리기
    roll(direction)
    # 다음 방향 구하기
    direction = next_direction(direction, ny, nx)
    
    b_count = get_score(nx, ny)
    score += graph[ny][nx] * b_count
    # score += graph[ny][nx] * count(nx, ny, 0)
    
    # 한칸 이동
    roll_dice(nx, ny, move_count-1, direction)
    return
    
n, m, move_count = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 주사위
dice = [1, 2, 3, 4, 5, 6] # 위, 뒤, 오른쪽, 왼쪽, 앞, 아래

# 방향(동서남북) => 인덱스 1부터 시작
dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, 1, -1]

score = 0
start_x = 0
start_y = 0

roll_dice(start_x, start_y, move_count, 1)
print(score)
