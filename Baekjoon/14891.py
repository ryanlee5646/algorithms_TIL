# 톱니바퀴
from sys import stdin
input = stdin.readline

# 개행 제거하고 문자열 입력 받기
wheels = [stdin.readline().rstrip() for i in range(4)] # N극은 0, S극은 1
rotate_turn = int(input())
rotate = [list(map(int, input().split())) for _ in range(rotate_turn)]

A[2] : B[6]
B[2] : C[6]
C[2] : D[6] 
# 초기
10101111
01111101
11001110
00000010

# 3번째 톱니바퀴 반시계 방향으로 회전
# C[2]:D[6]이 다름
# C 반시계 D 시계방향 회전
10101111
01111101
10011101
00000001
