from sys import stdin

input = stdin.readline

def fibonacci(N):
    global zero_count, one_count
    if (N == 0):
        zero_count+=1
        return 0
    elif (N == 1):
        one_count+=1
        return 1
    else:
        return fibonacci(N-1) + fibonacci(N-2)
    

T = int(input())

for t in range(T):
    N = int(input())
    zero_count = 0
    one_count = 0
    zoero
    fibonacci(N)
    print(f'zero: {zero_count}')
    print(f'one: {one_count}')
    