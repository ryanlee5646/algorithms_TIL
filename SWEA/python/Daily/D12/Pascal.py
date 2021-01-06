import sys
sys.stdin = open("Pascal.txt", "r")

T = int(input())

for t in range(1,T+1):
    N = int(input())
    tri = [[0]*(N+1) for i in range(N+1)]     # +[0] * (N-1)
    for i in range(N+1):
        for j in range(1,i+1):
            if i == 1:
                tri[i][j] = 1
            else:
                tri[i][j] = tri[i-1][j-1] + tri[i-1][j]

    print("#{}".format(t))
    for i in range(1,N+1):
        print(*tri[i][1:i+1])
    # for i in range(N):
    #     for j in range(1,N+1):
    #         tri[i][j] = tri[j-1]+tri[j]
    #






# def Pascal(y,x):
#     if x==0 or y==x:
#         return 1
#     return Pascal(y-1,x-1) + Pascal(y-1,x)
#
# for t in range(1,T+1):
#     N = int(input())
#     tri = [[0]*10 for i in range(10)]
#     Pascal(0,0)
#


