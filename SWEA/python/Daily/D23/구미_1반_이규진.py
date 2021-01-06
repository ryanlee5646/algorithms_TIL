import sys
sys.stdin = open("190319.txt", "r")

T = int(input())
for t in range(1,T+1):
    tc = int(input())
    data = []
    for i in range(10):
        data.append(list(map(int,input().split())))
    total_sum = []
# 가로 길이 합
    for y in range(10):
        temp = 0
        for x in range(10):
            temp += data[y][x]
        total_sum.append(temp)

# 세로 길이 합
    for x in range(10):
        temp = 0
        for y in range(10):
            temp += data[y][x]
        total_sum.append(temp)
    
# 대각선 길이 합
    left = 0
    right = 0
    for i in range(10):
        left += data[i][i]
        right += data[i][9-i]
    total_sum.append(left)
    total_sum.append(right)

    print("#{} {}".format(tc, abs(max(total_sum)-min(total_sum))))
