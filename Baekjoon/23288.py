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

# dice = [1, 2, 3, 4, 5, 6] # 위, 뒤, 오른쪽, 왼쪽, 앞, 아래
def roll(direction):
    if direction == 1: # 동쪽
        dice[0], dice[2], dice[5], dice[3] = dice[3], dice[0], dice[2], dice[5]
    elif direction == 2: # 서쪽
        dice[0], dice[2], dice[5], dice[3] = dice[2], dice[5], dice[3], dice[0]
    elif direction == 3: # 남쪽
        dice[0], dice[1], dice[5], dice[4] = dice[1], dice[5], dice[4], dice[0]
    else: # 북쪽
        dice[0], dice[1], dice[5], dice[4] = dice[4], dice[0], dice[1], dice[5]

def next_direction(direction):
    if dice[5] > graph[ny][nx]:
        if direction == 1: # 동 -> 남
            direction = 3
        elif direction == 3: # 남 -> 서
            direction = 2
        elif direction == 2: # 서 -> 북
            direction = 4
        else:   # 북 -> 동
            direction = 1    
    elif dice[5] > graph[ny][nx]:
        if direction == 1: # 동 -> 북
            direction = 4
        elif direction == 4: # 북 -> 서
            direction = 2
        elif direction == 2: # 서 -> 남
            direction = 3
        else: # 남 -> 동
            direction = 1  
    return direction

def count(nx, ny, block_count):
    if not  0 <= nx < m and 0 <= ny < n:
        return
    for i in range(1, 5):
        next_x = nx + dx[i]
        next_y = ny + dy[i]
        if graph[ny][nx] == graph[next_y][next_x]:
            
def roll_dice(start_x, start_y, move_count, direction):
    global score
    if move_count == 0:
        print(score)
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
    
    score += graph[ny][nx] * count(nx, ny, 0)
    
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

