# import sys
# sys.stdin = open('input.txt', 'r')

stack = [0]*100
top = -1

Info = [0] * 128 #char 1byte ASCII code 7bit
Data = input()

Info[ord(')')] = '('
Info[ord(']')] = '['
Info[ord('>')] = '<'
Info[ord('}')] = '{'

howmany = len(Data)
for i in range(howmany):
    if Data[i] == '('or Data[i] == '{' or Data[i] == '[' or Data[i] == '<':
        top += 1
        stack[top]=Data[i]

    elif Info[ord(Data[i])] == stack[top]:
        top -= 1
    else:
        top = 235232
        break

if top == -1:
    print("Right")
else:
    print("Wrong")