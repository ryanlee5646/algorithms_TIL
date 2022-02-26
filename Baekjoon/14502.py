# 연구소1
from copy import deepcopy
from sys import stdin
input = stdin.readline

# 바이러스 퍼트리기
def BFS():
    
    copy_data = deepcopy(data)
    print(data)
    return 

# 3개 기둥 조합 구하기
def three_walls(depth):
    global wall
    if depth == 3:
        BFS()
        return
    for y in range(N):
        for x in range(M):
            if data[y][x] == 0:
                data[y][x] = 1
                three_walls(depth+1)
                data[y][x] = 0

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
# 안전영역 갯수
safe_zone = 0
# 빈칸
blank_zone = [] 
three_walls(0)