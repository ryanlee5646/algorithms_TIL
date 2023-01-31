# 단어 뒤집기 2
from sys import stdin
input = stdin.readline

S = list(input().rstrip())

stack = []

tag_yn = False

for i in S:
  if i == "<": # 태그 시작이면 태그유무 flag = True 하고 문자열에 바로 추가해줌
    print(''.join(stack)[::-1], end='')
    stack = []
    tag_yn = True
    stack.append(i)
  elif i == ">": # 태그 종료면 태그유무 flag = False하고 문자열에 바로 추가해줌
    tag_yn = False
    stack.append(i)
    print(''.join(stack), end='') # 앞에서부터 출력
    stack = []
  else: # 일반문자열이면서 
    if tag_yn: # 태그에 해당하면 문자열 추가 
      stack.append(i)
    else: # 태그가 아니고
      if i == " ": # 공백이면 스택에 있는 문자 출력 후 공백추가
        print(''.join(stack)[::-1] + " ", end='')
        stack = []
      else: # 공백이 아니라면 stack에 추가
        stack.append(i)
      
if stack:
  print(''.join(stack)[::-1], end='')
  