# import sys
# sys.stdin = open('5097_회전.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    Queue = [0] * 1000
    front = 0
    rear = len(num_list)-1
    for i in range(len(num_list)):
        Queue[i] = num_list[i]

    for j in range(M+1):
        rear += 1
        Queue[rear] = Queue[j]
    print(f'#{t} {Queue[rear]}')


