import sys
sys.stdin = open("bi_password.txt", "r")

password = {
    '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
    '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9
}
T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    data = []
    for i in range(N):
        data.append(list(map(str, input())))
    index = 0
    found = False
    for y in range(N):
        for x in range(-1, 0 - len(data[y]) - 1, -1):
            if data[y][x] == '1':
                index = x
                found = True
                break
        if found:
            break
    stack = []
    for j in range(index, 0 - len(data[y]) - 1, -7):  # index=-11
        if len(data[y][j - 6:j + 1]) == 7:
            string = ''
            for k in data[y][j - 6:j + 1]:
                string += k
            if string in password:
                stack.append(password[string])
    stack1 = []
    for i in range(len(stack)):  # stack 리버스
        stack1.append(stack.pop(-1))
    sum1 = 0
    sum2 = 0

    for a in [0, 2, 4, 6]:
        sum1 += stack1[a]
    for b in [1, 3, 5]:
        sum2 += stack1[b]
    if ((sum1 * 3) + sum2 + stack1[-1]) % 10 == 0:
        print("#{} {}".format(t, sum(stack1)))
    else:
        print("#{} 0".format(t))


