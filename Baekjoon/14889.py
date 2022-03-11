# 스타트와 링크(시간초과 단계를 줄여야할듯)
from sys import stdin
from itertools import permutations
input = stdin.readline

def min_value_cal(start, link):
    global min_value
    # 각팀의 순열 구하기
    start_list = list(permutations(start, 2))
    link_list = list(permutations(link, 2))
    # 각각 팀의 값 구하기
    start_value = sum(S[i][j] for i, j in start_list)
    link_value = sum(S[i][j] for i, j in link_list)
    # 각 팀의 차이값 구하기
    result = abs(start_value - link_value)
    # 최소값 구하기
    min_value = min(min_value, result)
    return 

def combination(depth):
    if depth == int(N/2):
        start = []
        link = []
        for i, j in enumerate(visited):
            if j == 1:
                start.append(i)
            else:
                link.append(i)
                
        min_value_cal(start, link)
        
    for i in range(depth, N):
        if not visited[i]:
            visited[i] = 1
            combination(depth+1)
            visited[i] = 0

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
data = [i for i in range(N)]
min_value = 1e9
visited = [0] * N
tmp = []

combination(0)
print(min_value)