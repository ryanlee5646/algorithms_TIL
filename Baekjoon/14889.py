# 스타트와 링크(시간초과 단계를 줄여야할듯)
from sys import stdin
from itertools import combinations
input = stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
data = [i for i in range(N)]
min_value = 1e9

for i in zip(*S):
    print(i)

# # 스타트팀 조합 구하기
# for combination in combinations(data, int(N/2)):
#     visited = [0] * N
#     start_team = []
#     link_team = []
    
#     # 스타트팀 체크하기
#     for i in combination:
#         visited[i] = 1
#         start_team.append(i)
#     # 링크팀 구하기    
#     for i in range(N):
#         if not visited[i]:
#             link_team.append(i)
    
#     start_team_score = 0
#     link_team_score = 0
    
#     for i in range(int(N/2)):
#         for j in range(int(N/2)):
#             if i != j:
#                 start_team_score += S[start_team[i]][start_team[j]]
#                 link_team_score += S[link_team[i]][link_team[j]]

#     min_value = min(min_value, abs(start_team_score - link_team_score))

# print(min_value)