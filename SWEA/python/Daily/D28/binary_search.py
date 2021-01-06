import sys
sys.stdin = open("binary_search.txt", "r")

# A = [1, 3, 5, 7, 9]
# B = [1, 2, 3, 4, 5]

# def BiSearch():

T = int(input())
for t in range(1,T+1):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    count = 0
    for i in B:
        start = 0
        end = len(A)-1
        m = (start+end) // 2
        flag = 3
        while True:
            if i == A[m]: #들어오자마자 값이 있는경우
                count+=1
                break
            elif i < A[m]:
                if flag == 1: #비교하는 값이 m값보다 작은경우 left
                    break
                else:
                    end = m - 1
                    m = (start+end) // 2
                    flag = 1 #(왼쪽)
            elif i > A[m]:
                if flag == 2: #비교하는 값이 m값보다 큰 경우 right
                    break
                else:
                    start = m + 1
                    m = (start + end) // 2
                    flag = 2 #(오른쪽

    print("#{} {}".format(t,count))

