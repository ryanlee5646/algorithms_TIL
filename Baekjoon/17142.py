# 연구소3
import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline 
dx = [-1, 1, 0, 0] # 왼쪽, 오른쪽, 위, 아래
dy = [0, 0, -1, 1]

def BFS():
    
    return 

N, virus_num = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
virus_locate = []
answer = 987654321

# 바이러스 위치 정보
for y in range(N):
    for x in range(N):
        if data[y][x] == 2:
            virus_locate.append([y,x])
# 바이러스 조합
virus_combination = list(combinations(virus_locate, virus_num))



