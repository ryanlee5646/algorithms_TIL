import sys
sys.stdin = open("input.txt", 'r')


# Info = [0] * 128

T = int(input())

for t in range(T):
    stack = [0] * 100
    top = -1
    Blank = input()
    for i in Blank:
        if i == '(' or i == '{':
            top += 1
            stack[top] = i
        elif i == ')' or i =='}':
            if top == -1:
                print(f"#{t+1} {0}")
                break
            elif (stack[top] == '(' and i != ')') or (stack[top] == '{' and i != "}") :
                print(f"#{t+1} {0}")
                break
            else:
                stack[top] = 0
                top -= 1

    else:
        if top == -1:
            print(f"#{t+1} {1}")
        else:
            print(f"#{t+1} {0}")








# Info = [0] * 128

# T = int(input())
#
# for t in range(T):
#     stack = [0] * 10
#     top = -1
#
#     Blank = input()
#     for i in Blank:
#         print(stack)
#         if i == '(' or i == '{':
#             top += 1
#             stack[top] = i
#         elif i == ')' or i =='}':
#             if top == -1:
#                 print(f"#{t+1} {0}")
#                 break
#             elif (stack[top] == '(' and i != ')') or (stack[top] == '{' and i != "}") :
#                 print(f"#{t+1} {0}")
#                 break
#             else:
#                 stack[top] = 0
#                 top -= 1
#     else:
#         if top == -1:
#             print(f"#{t+1} {1}")
#         else:
#             print(f"#{t+1} {0}")












# ascii = [40, 41, 123, # 125] # 40='(', 41=')', 123='{', 125='



#if top==-1 and (i == ')' or i =='}'):
#     print(f"#{t+1} {0}")
#     break
# elif (top > -1 and stack[top] == '(' and i == '}') or (top > -1 and stack[top] == '{' and i == ')'):
#     print(f"#{t+1} {0}")
#     break
# elif i == '(' or i =='{':
#     top += 1
#     stack[top] = i
# elif stack[top] != i and stack[top] == '(' and top > -1 and i == ')':
#     stack[top] = 0
#     top -= 1
# elif stack[top] != i and stack[top] == '{' and top > -1 and i == '}':
#     stack[top] = 0
#     top -= 1