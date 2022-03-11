# 스타트와 링크
from sys import stdin
input = stdin.readline

def min_value_cal(start, link):
    global min_value
    start_value = S[start[0]][start[1]] + S[start[1]][start[0]]
    link_value = S[link[0]][link[1]] + S[link[1]][link[0]]
    result = abs(start_value - link_value)
    min_value = min(min_value, result)
    return 

def combination(depth):
    if depth == int(N/2):
        start = []
        link = []
        for i, j in enumerate(visited):
            print(f"index:{i} value:{j}")
            if j == 1:
                start.append(i)
            else:
                link.append(j)
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