import sys
sys.stdin = open("num_add_5018.txt", "r")

T = int(input)
# N: 수열의 길이 / M: 추가 횟수 / L: 출력할 인덱스 번호
for t in range(1,T+1):
    N, M, L = map(int,input().split())
