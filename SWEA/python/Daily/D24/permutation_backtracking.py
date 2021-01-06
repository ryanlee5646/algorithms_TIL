
# 순열
def Permutation(here, r):
    global count1
    if len(result) == r:
        count1 += 1
        print(result, end=' ')
        return
    for i in range(len(data)):
        if visited[i] == 0:
            visited[i] = 1
            result.append(data[i])
            Permutation(here+1,r)
            visited[i] = 0
            result.pop()
# 중복순열
def Mul_Permutation(here, r):
    global count2
    if len(result1) == r:
        count2 += 1
        print(result1, end=' ')
        return
    for i in range(len(data)):
        result1.append(data[i])
        Permutation(here+1,r)
        result1.pop()


data = [1,2,3]

result = []
visited = [0]*len(data)
count1 = 0
count2 = 0
DFS(0, 3)
print()
print(count1)
print()

result1 = []
Mul_DFS(0,3)

print()
print(count2)



# permu = []
# for a in range(N):
#     for b in range(N):
#         if a != b:
#             for c in range(N):
#                 if a != c and b != c:
#                     permu.append([data[a],data[b],data[c]])
#
# print(permu)
#
# # 중복순열
# mul_permu = []
# for a in range(N):
#     for b in range(N):
#         if a != b or a == b:
#             for c in range(N):
#                 if (a != c or b != c) or (a == c or b == c):
#                     mul_permu.append([data[a],data[b],data[c]])
# print(mul_permu)