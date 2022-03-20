# 톱니바퀴
from sys import stdin
input = stdin.readline

def rotate(wheel, rotate_dir):
    if rotate_dir == 1: # 시계방향
        wheels[wheel] = wheels[wheel][-1] + wheels[wheel][0:-1]
    else: # 반시계 방향
        wheels[wheel] = wheels[wheel][1:] + wheels[wheel][0]
    return

def check_wheel(wheel, rotate_dir):
    if wheel == 0: # 첫번째 바퀴
        if wheels[wheel][2] != wheels[wheel+1][6]: # 오른쪽 바퀴 체크
            rotate(wheel+1, rotate_dir * -1)
        rotate(wheel, rotate_dir)
    elif wheel == 1: # 두번째 바퀴
        if wheels[wheel-1][2] != wheels[wheel][6]: # 왼쪽바퀴 체크       
            rotate(wheel-1, rotate_dir * -1)
        if wheels[wheel][2] != wheels[wheel+1][6]: # 오른쪽 바퀴 체크
            rotate(wheel+1, rotate_dir * -1)
        rotate(wheel, rotate_dir)
        
    elif wheel == 2: # 두번째 바퀴
        if wheels[wheel-1][2] != wheels[wheel][6]: # 왼쪽바퀴 체크       
            rotate(wheel-1, rotate_dir * -1)
        if wheels[wheel][2] != wheels[wheel+1][6]: # 오른쪽 바퀴 체크
            rotate(wheel+1, rotate_dir * -1)
        rotate(wheel, rotate_dir)
    else:
        if wheels[wheel-1][2] != wheels[wheel][6]: # 왼쪽 바퀴 체크
            rotate(wheel-1, rotate_dir * -1)
        rotate(wheel, rotate_dir)
    return

# 개행 제거하고 문자열 입력 받기
wheels = [stdin.readline().rstrip() for i in range(4)] # N극은 0, S극은 1
rotate_turn = int(input())
wheel_and_rotate = [list(map(int, input().split())) for _ in range(rotate_turn)]
result = 0
for i in wheel_and_rotate:
    wheel, rotate_dir = i
    check_wheel(wheel-1, rotate_dir)

for i in range(4):
    result += (2**i) * int(wheels[i][0])

print(result)