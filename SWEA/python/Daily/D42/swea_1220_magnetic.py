import sys
sys.stdin = open("swea_1220_magnetic.txt")

T = 10
for t in range(1, 11):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    block = 0
    for x in range(N):
        stack = []
        for y in range(N):
            if data[y][x]:
                stack.append(data[y][x])
        # print(stack,"length {}".format(len(stack)))
        num = 1
        temp = [stack[0]]
        # print('temp', type(temp))
        # print(temp)
        while num < len(stack) :
            if temp[-1] == 1:
                if stack[num] == 1:
                    temp.append(stack[num])
                    num += 1
                elif stack[num] == 2:
                    temp.append(stack[num])
                    block += 1
                    # print(temp, "block", block)
                    num += 1

            else:
                temp.append(stack[num])
                num += 1

        # print("block",block)
    print('#{} {}'.format(t,block))

