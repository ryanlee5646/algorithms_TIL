import sys
sys.stdin = open("2001_beat_pari.txt", "r")

T = int(input())

for t in range(1,T+1):
    N, M = map(int, input().split())
    data = []
    max_list = []
    for i in range(N):
        data.append(list(map(int, input().split())))
    for y in range(N-M+1):
        for x in range(N-M+1):
            temp_max = 0
            for a in range(M):
                for b in range(M):
                    temp_max += data[y+a][x+b]
            max_list.append(temp_max)
    print("#{} {}".format(t, max(max_list)))

