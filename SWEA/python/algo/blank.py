    # import sys
# sys.stdin = open("input.txt", "r")

stack = [0]*10
top = -1

Data = input()

for i in Data:
    if i == '(': # stack 인덱스 처음부터 열리는 괄호를 채워줌
        top+= 1
        stack[top] = i
        print(stack)

    elif stack[top] != i and top > -1: #열리는 괄호가 아니라면 마지막 열린괄호를 짝지어줌. 짝이 맞으면 마지막 열린괄호를 0으로 초기화 후 top을 감소
        stack[top] = 0
        top-=1
        print(stack)
    else:
        print("송현우")
        break
else:
    if top == -1 :
        print('진민재')
    else:
        print('송현우')

