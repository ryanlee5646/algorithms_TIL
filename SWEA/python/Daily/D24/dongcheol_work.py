import sys
sys.stdin = open("dongcheol_work.txt", "r")


# def Back(yy):
#     global max_result
#     if len(permutation) == N:
#         temp = 1
#         for i in permutation:
#             temp*=i
#         if max_result == 1 or temp > max_result:
#             max_result = temp
#             return
#     if len(permutation) < N:
#         temp = 1
#         for i in permutation:
#             temp*=i
#             # print(temp)
#         if max_result != 1 and max_result >= temp:
#             return
#     for xx in range(N):
#         if not visited[xx]:
#             visited[xx] = 1
#             permutation.append(data[yy][xx])
#             Back(yy+1)
#             visited[xx] = 0
#             permutation.pop()
# T = int(input())
# for t in range(1,T+1):
#     N = int(input())
#     data = []
#     visited = [0]*N
#     max_result = 1
#     permutation = []
#     for i in range(N):
#         data.append(list(map(int,input().split())))
#     for y in range(N):
#         for x in range(N):
#             data[y][x] /= 100
#     Back(0)
#     A=round(max_result*100)
#     A=format(A,".6f")
#     print("#{} {}".format(t,A))


def Back(yy, now_temp):
    global max_result
    if yy == N:
        if now_temp > max_result:
            max_result = now_temp
            return
    if now_temp <= max_result:
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            Back(yy+1, now_temp*data[yy][i])
            visited[i] = 0
T=int(input())
for t in range(1,T+1):
    N = int(input())
    data = []
    visited = [0]*N
    max_result = 0
    for i in range(N):
        data.append(list(map(int,input().split())))
    for y in range(N):
        for x in range(N):
            data[y][x] *= 0.01
    Back(0,1)
    A = max_result * 100
    A = format(A, ".6f")
    print("#{} {}".format(t,A))


