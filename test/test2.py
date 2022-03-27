from collections import deque
# tc1
n = 4
clockwise = True

# tc2
# n = 6
# clockwise = False

# tc3
# n = 9
# clockwise = False

def rotate(y, x, direction, move, num):
    global clockwise
    if move == 1:
        y = y + dir_y[direction]
        x = x + dir_x[direction]
        data[y][x] = num
        return
    if move == 0:
        return
    
    for i in range(move):
        data[y][x] = num
        y = y + dir_y[direction]
        x = x + dir_x[direction]
        num+=1
    
    if clockwise == True:
        if direction == 0:
            rotate(y, x, 1, move-2, num)
        elif direction == 1:
            rotate(y, x, 2, move-2, num)
        elif direction == 2:
            rotate(y, x, 3, move-2, num)
        else:
            rotate(y, x, 0, move-2, num)
    
    else:
        if direction == 0:
            rotate(y, x, 3, move-2, num)
        elif direction == 1:
            rotate(y, x, 0, move-2, num)
        elif direction == 2:
            rotate(y, x, 1, move-2, num)
        else:
            rotate(y, x, 2, move-2, num)
    return

# n = int(input())
# clockwise = input()

dir_y = [0, 1, 0, -1] # 오른쪽, 아래, 왼쪽, 위 (시계방향)
dir_x = [1, 0, -1, 0]

data = [[0]*n for i in range(n)]

if n < 3:
    for i in range(n):
        for j in range(n):
            data[i][j] = 1
else:
    if clockwise == True:
        start_point = [[0, 0, 0], [0, n-1, 1], [n-1, 0, 3], [n-1, n-1, 2]]
    else:
        start_point = [[0, 0, 1], [0, n-1, 2], [n-1, 0, 0], [n-1, n-1, 3]]
    
    # True: 시계방향 / False: 반시계방향
    for start in start_point:
        y, x, direction = start
        rotate(y, x, direction, n-1, 1) # y좌표, x좌표, 방향, 이동횟수, 숫자, clockwise 
print(data)