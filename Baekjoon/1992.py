# 쿼드트리
from sys import stdin
input = stdin.readline

def quad_tree(y, x, n):
  flag = data[y][x] # 초기 값 설정
  for i in range(y, y+n):
    for j in range(x, x+n):
      if flag != data[i][j]: # 탐색중 초기값이랑 다르면 flag -1로 수정
        flag = '-1'
        break
      
  if flag == '-1': # 분할하기전 괄호 만들어주고 탐색
    print("(", end="")
    n = n // 2
    quad_tree(y, x, n)
    quad_tree(y, x+n, n)
    quad_tree(y+n, x, n)
    quad_tree(y+n, x+n, n)
    print(")", end="")

  elif flag == '0': # 전부다 0
    print(0, end="")
  else:
    print(1, end="") # 전부다 1

N = int(input())

data = [list((input().rstrip())) for i in range(N)]

quad_tree(0, 0, N)
