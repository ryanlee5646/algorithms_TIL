# 종이의 개수
import sys
read = sys.stdin.readline

def count(check_num):
    global minus, zero, plus
    # 종이에 숫자가 다 같으면 더해주기
    if check_num == -1:
        minus += 1
    elif check_num == 0:
        zero += 1
    else:
        plus += 1

def check(start_y, start_x, N):
    # 체크할 숫자
    check_num = data[start_y][start_x]
    # 종이가 한장이면 리턴
    if N == 1:
        count(check_num)
        return
    for y in range(start_y, start_y + N):
        for x in range(start_x, start_x + N):
            # 종이가 숫자가 다른게 나오면 
            if check_num != data[y][x]:
                # 9등분 했을 때 각각 종이에서 왼쪽 위 시작점 좌표로 재귀호출
                for _y in range(3):
                    for _x in range(3):
                        # 시작점 좌표를 위 아래롤 3씩 이동하면서 9등분 체크
                        check(start_y+N//3*_y, start_x+ N//3*_x, N//3)
                return
    count(check_num)

N = int(input())
data = [list(map(int, read().split())) for _ in range(N)]
    
minus = 0
zero = 0
plus = 0

check(0, 0, N)
print(minus)
print(zero)
print(plus)