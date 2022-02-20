# N과 M(9)
from sys import stdin
input = stdin.readline

# def combinations(start):
#     if len(tmp) == M:
#         result = ' '.join(map(str, tmp))
#         # print(' '.join(map(str, tmp)))
#         if result not in duplication_check:
#             duplication_check.append(result)
#         return 
#     for i in range(len(data)):
#         if not visited[i]:
#             visited[i] = 1
#             tmp.append(data[i])
#             combinations(start+1)
#             visited[i] = 0
#             tmp.pop() 

# N, M = map(int, input().split())
# data = list(map(int, input().split()))
# data.sort()
# tmp = []
# # 중복을 체크하는 배열(pypy로는 통과되는데 python으로 돌리면 시간초과남)
# duplication_check = []
# visited = [0] * N

# combinations(0)
# for i in duplication_check:
#     print(i)
    
def combinations(start):
    if len(tmp) == M:
        check = ' '.join(map(str, tmp))
        if check not in dic:
            dic[check] = 1
            print(check)
        return
    for i in range(len(data)):
        if not visited[i]:
            visited[i] = 1
            tmp.append(data[i])
            combinations(start+1)
            visited[i] = 0
            tmp.pop() 

N, M = map(int, input().split())
data = sorted(list(map(int, input().split())))
tmp = []
visited = [0] * N
# 중복을 체크하는 딕셔너리
# ({'1 7': 1, '1 9': 1, '7 1': 1, '7 9': 1, '9 1': 1, '9 7': 1, '9 9': 1})
dic = {}
combinations(0)