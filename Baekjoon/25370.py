# 카드 숫자 곱의 경우의 수 

from sys import stdin
input = stdin.readline

def combination(depth):
  if  len(tmp) == n:
    num = 1
    for i in range(n):
      num *= tmp[i]
    # if num not in result:
    result.append(num)
    return
  
  for i in range(depth, len(data)):
        tmp.append(data[i])
        combination(i)
        tmp.pop() 
  
  
n = int(input())
data = [1,2,3,4,5,6,7,8,9]
tmp = []
result = []

combination(0)
print(len(set(result)))