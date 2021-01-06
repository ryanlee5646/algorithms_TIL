import sys
sys.stdin = open("cal.txt","r")

def cal(depth, sum):
    global result
    if depth == N:
        if sum > result:
            result = sum
        return

    cal(depth+1, sum+data[depth])
    cal(depth+1, sum*data[depth])

T = int(input())
for t in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    result = 0

    cal(1,data[0])t
    print(f"#{t} {resul}")