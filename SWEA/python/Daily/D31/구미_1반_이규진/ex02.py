import sys,time
sys.stdin = open("ex02.txt", "r")
from itertools import combinations
stime = time.time()
# def combi(index,combination,length):
#     if len(combination) == length:
#         print(combination)
#         return
#
#     if index >= len(order):
#         return
#
#     combination(index+1,combination+[order[index]],length)
#     combination(index+1,combination,length)
#
# order = [0,1,2,3,4,5]
#
# combi(0,[],3)


T = int(input())
for t in range(1,T+1):
    N, M = map(int,input().split()) # N = 행 , M = 열
    data = []
    max_sum = 0
    for i in range(N):
        data.append(list(map(int,input().split())))
    order = list(combinations([0, 1, 2, 3, 4, 5], 3))

    for y in range(1, N):  # 가로줄 선택
        for x1 in range(1,M-1):  # 첫번째 세로 줄 선택
            for x2 in range(x1+1, M):  # 두번째 세로 줄 선택 // 줄선택완료
                region1 = region2 = region3 = 0
                for horizon123 in range(y):  # 1, 2, 3 구간의 합
                    region1 += sum(data[horizon123][:x1])
                    region2 += sum(data[horizon123][x1:x2])
                    region3 += sum(data[horizon123][x2:])
                region4 = region5 = region6 = 0
                for horizon456 in range(y,N): # 4, 5, 6 구간의 합
                    region4 += sum(data[horizon456][:x1])
                    region5 += sum(data[horizon456][x1:x2])
                    region6 += sum(data[horizon456][x2:])

                result =[region1,region2,region3,region4,region5,region6] #각 구간별 합
                for i in order:
                    temp = 0
                    temp += abs(result[i[0]]-result[i[1]]) + abs(result[i[1]] - result[i[2]]) + abs(result[i[2]] - result[i[0]])

                    if temp >= max_sum:
                        max_sum = temp

    print("#{} {}".format(t,max_sum))
    print(time.time() - stime)









