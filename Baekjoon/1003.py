from sys import stdin

input = stdin.readline

def fibonacci(N):
    # 점화식 구하기
    for i in range(3, N):
        zero.append((zero[i-2] + zero[i-1]))
        one.append((one[i-2] + one[i-1])) 
    return

T = int(input())
zero = [1, 0, 1]
one = [0, 1, 1]

# 배열에 미리 담아놓기
fibonacci(40)

result = []
for t in range(T):
    N = int(input())
    print(f'{zero[N]} {one[N]}')
    # result.append([zero[N], one[N]])
for i,j in result:
    print(i, end=' ')
    print(j)