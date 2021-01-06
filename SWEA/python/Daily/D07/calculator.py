import sys
sys.stdin = open("calculator.txt", "r")

# (6+5*(2-8)/2) => 6528-*2/+
for t in range(1, 11):
    a = input()
    # operator = ['(', '+','-','*','/']
    stack = []
    nums = []
    Data = input()
    for i in Data:
        if i.isdecimal():
            nums.append(i)
        else:
            if stack == [] or i == '(' or i == '*' or i == '/':
                stack.append(i)
            elif i == '+' or i =='-':
                if stack[-1] == '*' or stack[-1] == '/':
                    while len(stack)!=0 and stack[-1] == '*' or stack[-1] == '/':
                        nums.append(stack.pop())
                stack.append(i)
            elif i == ')':
                while len(stack) > 0 and stack[-1] != '(':
                    nums.append(stack.pop())
                stack.pop()

    stack = []
    Decimal = []

    for i in nums:
        if i.isdecimal():
            stack.append(int(i))
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

    print(f'#{t} {stack[0]}')
