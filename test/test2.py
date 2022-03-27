# 0:오른쪽, 1:아래, 2:왼쪽, 3:위
def rotate(y, x, direction, move, num):
    global n, clockwise
    
    if move == 1: # 짝수일 경우 종료조건
        y = y + dir_y[direction]
        x = x + dir_x[direction]
        data[y][x] = num
        return
    if move == 0: # 홀수일 경우 종료조건
        data[y][x] = num
        return
    
    for i in range(move):
        data[y][x] = num
        y = y + dir_y[direction]
        x = x + dir_x[direction]
        num+=1
    # 다음 시작점으로 초기화 (위에서 무조건 + 시키기 때문에)
    y = y - dir_y[direction] 
    x = x - dir_x[direction]
    
    if clockwise == True: # 시계방향
        if direction == 0:
            rotate(y + dir_y[1], x + dir_x[1], 1, move-2, num)
        elif direction == 1:
            rotate(y + dir_y[2], x + dir_x[2], 2, move-2, num)
        elif direction == 2:
            rotate(y + dir_y[3], x + dir_x[3], 3, move-2, num)
        else:
            rotate(y + dir_y[0], x + dir_x[0], 0, move-2, num)
    
    else: # 반시계 방향
        if direction == 0:
            rotate(y + dir_y[3], x + dir_x[3], 3, move-2, num)
        elif direction == 1:
            rotate(y + dir_y[0], x + dir_x[0], 0, move-2, num)
        elif direction == 2:
            rotate(y + dir_y[1], x + dir_x[1], 1, move-2, num)
        else:
            rotate(y + dir_y[2], x + dir_x[2], 2, move-2, num)
    return

n = int(input())
clockwise = False

dir_y = [0, 1, 0, -1] # 오른쪽, 아래, 왼쪽, 위 (시계방향)
dir_x = [1, 0, -1, 0]

data = [[0]*n for i in range(n)]

if n < 3: # N이 1 혹은 2일 경우 모두 1넣고 초기화
    for i in range(n):
        for j in range(n):
            data[i][j] = 1
else:
    if clockwise == True:
        start_point = [[0, 0, 0], [0, n-1, 1], [n-1, n-1, 2], [n-1, 0, 3]]
    else:
        start_point = [[0, 0, 1], [0, n-1, 2], [n-1, n-1, 3], [n-1, 0, 0]]
    
    # True: 시계방향 / False: 반시계방향
    for start in start_point:
        y, x, direction = start
        rotate(y, x, direction, n-1, 1) # y좌표, x좌표, 방향, 이동횟수, 숫자, clockwise 
print(data)