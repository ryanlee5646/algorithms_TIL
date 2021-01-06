import sys
sys.stdin = open("swea_3431","r")

T = int(input())
for t in range(1, T+1):
    low, high, now = map(int,input().split())
    result = 0

    if low <= now <= high:
        print("#{} 0".format(t))

    elif now > high:
        print("#{} -1".format(t))

    else:
        result = low - now
        print("#{} {}".format(t, result))