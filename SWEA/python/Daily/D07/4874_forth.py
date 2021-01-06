import sys
sys.stdin = open("4874.txt", "r")

T = int(input())

# 10 2 + 3 4 + * .
for t in range(1, T+1):
    flag = True
    stack = []
    Decimal = []
    Data = input().split()

    for num in Data:
        if num.isdecimal():
            Decimal.append(num)

    if len(Decimal) == (len(Data)-len(Decimal)): #테스트 케이스 맨 뒤에 '.'이 있기 때문에 정수 개수랑 연산자 개수가 동일할 때 실행
        for i in Data:
            if i.isdecimal():
                stack.append(int(i))

            else:
                if i != '.' and len(stack) < 2:
                    flag = False
                    break
                elif i == '+' and len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b)+int(a))
                elif i == '-' and len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b) - int(a))
                elif i == '*' and len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b) * int(a))
                elif i == '/' and len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b/a))
    else:
        flag = False
    if flag == True:
        print(f'#{t} {stack[0]}')
    else:
        print(f'#{t} error')

