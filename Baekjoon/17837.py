# 새로운 게임2
'''
0:흰색, 1:빨간색, 2:파란색
y,x,이동방향

4 4
0 0 2 0
0 0 1 0
0 0 1 2
0 2 0 0
2 1 1 => (2,1) 오른쪽
3 2 3 => (3,2) 위쪽
2 2 1 => (2,2) 오른쪽
4 1 2 => (4,1) 왼쪽

#1. 흰색 칸 이동한 경우:
  1. 이동하려는 말 기준으로 위로 쌓인 말은 같이 이동한다.
  2. 기존에 있는 말 위로 쌓인다 => ABC -> DE = DEABC
#2. 빨간색 칸 인 경우
  1. 이동한 후 말의 순서가 뒤바뀜 ABC -> CBA
  2. 이동한 칸에 말이 있는 경우 => ABC -> DE = DECBA
#3. 파란색 칸 인 경우, 칸을 벗어 난 경우
  1. 방향을 반대로 바꾼 후 이동
  2. 방향을 바꾼 후 반대로 이동하려는 칸이 또 파란색이면 가만히 있는다.
'''

from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
chess_infos = [list(map(int, input().split())) for _ in range(k)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

print(graph)
print(chess_infos)
