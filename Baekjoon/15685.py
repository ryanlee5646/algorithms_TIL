# 드래곤 커브
from sys import stdin
input = stdin.readline

'''
0: x좌표가 증가하는 방향
1: y좌표가 감소하는 방향
2: x좌표가 감소하는 방향
3: y좌표가 증가하는 방향 
'''

N = int(input())  # 커브의 개수
info = [list(map(int, input().split())) for _ in range(N)]
graph = [[0]*100 for _ in range(100)]
print(info)
print(graph)
