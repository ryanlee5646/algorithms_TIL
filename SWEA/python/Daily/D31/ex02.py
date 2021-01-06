import sys, itertools, time
sys.stdin = open("ex02.txt", "r")
stime = time.time()

combination = list(itertools.combinations([0,1,2,3,4,5],3))
print(combination)

T = int(input())
for t in range(1,T+1):
    N, M = map(int,input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for y in range(1,N):
        for x1 in range(1,M-1):
            for x2 in range(x1+1, M):
                a1 = a2 = a3 = 0
                for y1 in range(y):
                    a1+=sum(data[y1][:x1])
                    a2+=sum(data[y1][x1:x2])
                    a3+=sum(data[y1][x2:])
                a4 = a5 = a6 = 0
                for y2 in range(y,N):
                    a4+=sum(data[y2][:x1])
                    a5+=sum(data[y2][x1:x2])
                    a6+=sum(data[y2][x2:])
                sum_list = [a1,a2,a3,a4,a5,a6]
                for i in combination:
                    if abs(sum_list[i[0]]-sum_list[i[1]]) + abs(sum_list[i[1]]-sum_list[i[2]]) + abs(sum_list[i[2]]-sum_list[i[0]]) > result:
                        result = abs(sum_list[i[0]]-sum_list[i[1]]) + abs(sum_list[i[1]]-sum_list[i[2]]) + abs(sum_list[i[2]]-sum_list[i[0]])
    print("#{} {}".format(t, result))
    print(time.time() - stime)
