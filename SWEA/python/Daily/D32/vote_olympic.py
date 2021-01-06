import sys
sys.stdin = open("vote_olympic.txt", "r")

T = int(input())
for t in range(1,T+1):
    N, M = map(int,input().split())
    game = list(map(int,input().split()))
    people = list(map(int,input().split()))
    vote = [0] * N
    for p in people:
        for i, value in enumerate(game):
            if p >= value:
                vote[i] += 1
                break
    print("#{} {}".format(t,vote.index(max(vote))+1))
