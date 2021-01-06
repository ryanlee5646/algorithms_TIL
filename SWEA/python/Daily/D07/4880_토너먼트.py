import sys
sys.stdin = open("4880_토너먼트.txt", "r")

T = int(input())
# 1 : 가위 , 2 : 바위, 3: 보
for t in range(1, T+1):
    people = int(input())
    card = list(map(int, input().split()))
    group_A = card[:len(card)//2+1]
    group_B = card[(len(card)//2)+1:]
    print(group_A)
    print(group_B)
