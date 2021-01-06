import sys
sys.stdin = open("bi_tree_2263.txt", "r")

# 후위 데이터에서 맨마지막 값이 항상 루트가 됨
# 그다음에 중위 데이터에서 루트값을 기준으로 left, right를 나눔
# 다시 후위 데이터에서 left값 right값 기준으로 루트를 찾고
# 중위데이터에서 left right를 나눔

T = int(input())
for t in range(1,T+1):
    in_od = list(map(int, input().split()))
    post_od = list(map(int, input().split()))

    print(in_od)