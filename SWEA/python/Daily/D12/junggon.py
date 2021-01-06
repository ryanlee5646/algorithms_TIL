import sys
sys.stdin = open("junggon.txt", "r")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    num_list1 = list(map(int, input().split()))
    num_list2 = num_list1  #[2, 4, 7, 10]
    danjo = []
    result = []
    Max = []
    for i in num_list1:
        for j in num_list2:
            if i != j:
                danjo.append(i*j)
    print(danjo)
    for j in danjo:
        if  j >10 and j%10 != 0:
            result.append(j)
    print(result)
    for k in result:
        data = str(k)
        if ord(data[0]) < ord(data[1]):
            Max.append(int(data))
    print(Max)


    print("#{} {}".format(t,max(Max)))

T = int(input())
for t in range(T):
    N = int(input()) #[2, 4, 7, 10]
    num_list = list(map(int, input().split()))
    Max = 0
    for i in range(N-1): # [0, 1, 2, 3]
        for j in range(i + 1, N):
            mul = num_list[i] * num_list[j]
            temp = mul
            while temp // 10: # 123
                a = temp % 10 # 끝자리 수
                temp //= 10
                if a < (temp % 10):
                    break
            else:
                if Max < mul:
                    Max = mul

    if Max:
        result = Max
    else:
        result = -1

    print('#{} {}'.format(t+1, result))

