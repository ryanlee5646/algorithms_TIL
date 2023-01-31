from sys import stdin
input = stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in arr:
    scores = i[1:]
    mean = round(sum(scores)/len(scores), 3)
    count = 0
    for j in scores:
        if j > mean:
            count += 1

    print('{:.3f}%'.format(round(count/len(scores)*100, 3)))