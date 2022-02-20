# N과 M(12)
# from sys import stdin
# from itertools import *
# input = stdin.readline

# 방법 1
# def combination(start):
#     if start == M:
#         check = ' '.join(map(str, tmp))
#         if check not in dic:
#             dic[check] = 1
#             print(check)
#         return
#     for i in range(len(data)):
#         if len(tmp):
#             if tmp[-1] > data[i]:
#                 continue
#         tmp.append(data[i])
#         combination(start+1)
#         tmp.pop()
        
# N, M = map(int, input().split())
# data = sorted(list(map(int, input().split())))
# tmp = []
# dic = {}
# combination(0)

# 방법 2
from sys import stdin
from itertools import *
input = stdin.readline

N, M = map(int, input().split())
data = list(map(int, input().split()))

result = sorted(set(list(combinations_with_replacement(sorted(data), M))))
for i in result:
    print(*i)