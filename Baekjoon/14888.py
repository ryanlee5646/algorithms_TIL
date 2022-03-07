# 연산자 끼워넣기
from sys import stdin
input = stdin.readline

def DFS(depth, result, plus, minus, multiply, division):
    global max_value, min_value
    if depth == N:
        max_value = max(result, max_value)
        min_value = min(result, min_value)
        return
    if plus > 0 :
        DFS(depth + 1, result + num_list[depth], plus-1, minus, multiply, division)
    if minus > 0 :
        DFS(depth + 1, result - num_list[depth], plus, minus-1, multiply, division)
    if multiply > 0:
        DFS(depth + 1, result * num_list[depth], plus, minus, multiply-1, division)
    if division > 0:
        DFS(depth + 1, int(result / num_list[depth]), plus, minus, multiply, division-1)

N = int(input())
num_list = list(map(int, input().split()))
operator = list(map(int, input().split()))
max_value = -1000000001
min_value = 1000000001

DFS(1, num_list[0], operator[0], operator[1], operator[2], operator[3])

print(max_value)
print(min_value)

