
def combination(data, r):
    global Data
    # 1.
    data = sorted(data)

    # 2.
    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            return

        # 3.
        if chosen:
            start = data.index(chosen[-1]) + 1
        else:
            start =0
        for nxt in range(start, len(data)):
            chosen.append(data[nxt])
            generate(chosen)
            chosen.pop()

    generate([])

combination([1, 2, 3, 4], 4)



    # global result, data
    # if start == len(data):
    #     return
    # if len(result) < r:
    #     result.append(data[start])
    # else:
    #     return
    #
    #
    # combination(start+1, r)
    # combination(start, r)




T = int(input())
for t in range(T):
    N = int(input())
    Data = list(map(int, input().split()))
    max_mul = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            mul = Data[i] * Data[j]
            temp = mul
            while temp // 10:
                a = temp % 10
                temp //= 10
                if a < (temp % 10):
                    break
            else:
                if max_mul < mul:
                    max_mul = mul

    if max_mul:
        answer = max_mul
    else:
        answer = -1