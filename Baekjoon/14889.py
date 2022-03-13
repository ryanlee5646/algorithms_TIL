# 스타트와 링크
from sys import stdin
from itertools import combinations
input = stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
data = [i for i in range(N)]
min_score = 1e9

### 풀이1 ###
# 점수 계산
# def cal_score(start_team, link_team):
#     start_team_score = 0
#     link_team_score = 0
    
#     for i in range(len(start_team)):
#         for j in range(len(start_team)):
#             start_team_score += S[start_team[i]][start_team[j]]
#             link_team_score += S[link_team[i]][link_team[j]]

#     return abs(start_team_score - link_team_score)

# def combination(start_team, depth, start):
#     global min_score
#     # 링크팀 구하기
#     if depth == N//2:
#         link_team = []
#         for i in range(N):
#             if i not in start_team:
#                 link_team.append(i)

#         tmp_score = cal_score(start_team, link_team)
#         min_score = min(min_score, tmp_score)
#         return
    
#     # 스타트팀 구하기
#     for i in range(start, N):
#         if i not in start_team:
#             start_team.append(i)
#             combination(start_team, depth+1, i+1)
#             start_team.pop()

# combination([], 0, 0)

# print(min_score)

### 풀이2 (라이브러리 조합 + reversed) ###

# 점수 계산
# def cal_score(start_team, link_team):
#     start_team_score = 0
#     link_team_score = 0
    
#     for i in range(len(start_team)):
#         for j in range(len(start_team)):
#             start_team_score += S[start_team[i]][start_team[j]]
#             link_team_score += S[link_team[i]][link_team[j]]

#     return abs(start_team_score - link_team_score)

# # 스타트팀 / 링크팀 구하기
# start_combi = list(combinations(data, int(N/2)))
# link_combi = list(reversed(start_combi)) # 스타트님 조합을 뒤집으면 링크팀이 됌
# # start_combi: [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
# # link_combi: [(2, 3), (1, 3), (1, 2), (0, 3), (0, 2), (0, 1)]

# for i in range(len(start_combi) // 2):
#     min_score = min(min_score, cal_score(start_combi[i], link_combi[i]))

# print(min_score)


### 풀이3 (zip사용) ###

rows_sum = [sum(row) for row in S]
cols_sum = [sum(col) for col in zip(*S)]
# stat_by_member = [x + y for x, y in zip(rows_sum, cols_sum)]
stat_by_member = [sum(x) for x in zip(rows_sum, cols_sum)]
total = sum(rows_sum)
min_score = min(abs(total - sum(stats)) for stats in combinations(stat_by_member, int(N/2)))

print(f"zip(*S):{list(zip(*S))}")
print(f"rows_sum:{rows_sum}")
print(f"cols_sum:{cols_sum}")
print(f"zip(rows_sum, cols_sum): {list(zip(rows_sum, cols_sum))}")
print(f"stat_by_member:{stat_by_member}")
print(f"total: {total}")

print(min_score)