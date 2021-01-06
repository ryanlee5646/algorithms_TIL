import sys
sys.stdin = open("problem1.txt", "r")


T = int(input())
for t in range(1,T+1):
    fruits = []
    N, K = map(int, input().split())
    for i in range(N):
        fruits.append(list(map(int,input().split())))
    # print(fruits)
    result = []
    for y in range(N-K+1):
        for x in range(N-K+1):
            right = []
            left = []
            for i in range(K): # 0,1,2
                left.append(fruits[y+i][x+i]) #왼쪽 대각선
                right.append(fruits[y+i][x+(K-1)-i]) # 오른쪽 대각선
            result.append(abs(sum(left)-sum(right)))
    # print(result)
    print("#{} {}".format(t, min(result)))




