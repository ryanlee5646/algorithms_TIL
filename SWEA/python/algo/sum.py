import sys
sys.stdin = open("sum.txt","r")


for t in range(10):
    a = input()
    data = []
    result = []
    for y in range(100):
        x = list(map(int, input().split()))
        data.append(x)

    num_sum = []
    for i in data: # x축 합
        num_sum.append(sum(i))

    for i in range(100): # y축 합
        num_sum = []
        for j in range(100):
            num_sum.append(data[j][i])
        result.append(sum(num_sum))

    num_sum1 = []
    num_sum2 = []
    for i in range(100): # 대각선 합
        num_sum1.append(data[i][i])
        num_sum2.append(data[i][4-i])
    result.append(sum(num_sum1))
    result.append(sum(num_sum2))


    print(f'#{t+1} {max(result)}')