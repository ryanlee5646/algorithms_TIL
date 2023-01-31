from sys import stdin
input = stdin.readline

pipes = list(input().rstrip())

stack = []

result = 0

for i in range(len(pipes)):
  if pipes[i] == '(':
    stack.append(pipes[i])
  
  else: # ')' 일경우
    if pipes[i-1] == '(': # 레이저라면
      stack.pop()
      result += len(stack)
    else: # 파이프의 끝이라면
      result += 1
      stack.pop()

print(result)
    