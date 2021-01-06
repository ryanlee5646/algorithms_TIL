import sys

sys.stdin = open('input.txt', 'r')

for t in range(10):

    Data = []
    ladder_x = 0
    ladder_y = 99

    T = int(input())
    for i in range(100):  # 빈 리스트에 값을 입력 받음
        Data.append(list(map(int, input().split())))
    for x in range(100):  # 가장 아래 열에서 숫자 2를 찾음
        if Data[ladder_y][x] == 2:
            ladder_x = x
            break

    while True:
        if ladder_x - 1 >= 0 and Data[ladder_y][ladder_x - 1] == 1:
            Data[ladder_y][ladder_x] = 2
            ladder_x -= 1

        elif ladder_x + 1 < 100 and Data[ladder_y][ladder_x + 1] == 1:
            Data[ladder_y][ladder_x] = 2
            ladder_x += 1

        elif ladder_y == 0:
            print(f'#{t + 1} {ladder_x}')
            break
        else:
            Data[ladder_y][ladder_x] = 2
            ladder_y -= 1


