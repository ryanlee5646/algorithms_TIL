# 톱니바퀴
from sys import stdin
input = stdin.readline

def rotate(wheel, rotate_dir):
    if rotate_dir == 1: # 시계방향
        wheels[wheel] = wheels[wheel][7] + wheels[wheel][0:7]
    else: # 반시계 방향
        wheels[wheel] = wheels[wheel][1:8] + wheels[wheel][0]
    return

# 왼쪽 돌릴거 체크
def left_wheel_rotate(wheel, rotate_dir):
    if wheel-1 < 0:
        return
    if wheels[wheel-1][2] != wheels[wheel][6]:
        left_wheel_rotate(wheel-1, rotate_dir * -1)
        rotate(wheel-1, rotate_dir * -1)
# 오른쪽 돌릴거 체크
def right_wheel_rotate(wheel, rotate_dir):
    if wheel+1 > 3:
        return
    if wheels[wheel][2] != wheels[wheel+1][6]:
        right_wheel_rotate(wheel+1, rotate_dir * -1)
        rotate(wheel+1, rotate_dir * -1)

# 개행 제거하고 문자열 입력 받기
wheels = [stdin.readline().rstrip() for i in range(4)] # N극은 0, S극은 1
rotate_turn = int(input())
wheel_and_rotate = [list(map(int, input().split())) for _ in range(rotate_turn)]
result = 0
for i in wheel_and_rotate:
    wheel, rotate_dir = i
    right_wheel_rotate(wheel-1, rotate_dir) # 오른쪽 돌릴거 돌리고
    left_wheel_rotate(wheel-1, rotate_dir) # 왼쪽 돌릴거 돌리고
    rotate(wheel-1, rotate_dir) # 기준 바퀴 돌리고

for i in range(4):
    result += (2**i) * int(wheels[i][0])

print(result)