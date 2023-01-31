from sys import stdin
input = stdin.readline

N = int(input())

data = list(map(int, input().split()))
result = []

#1. 시간 초과남
# for i in range(len(data)):
#   data2 = data[i+1:]
#   if len(data2) == 0:
#       result.append(-1)
#       break
#   for j in range(len(data2)):  
#     if data[i] < data2[j] :
#       result.append(data2[j])
#       break
#     if len(data2)-1 == j:
#       result.append(-1)
#       break

# print(*result)

