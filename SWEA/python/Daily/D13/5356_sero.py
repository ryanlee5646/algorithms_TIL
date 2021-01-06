import sys
sys.stdin = open("5356_sero.txt", "r")

T = int(input())

for t in range(1,T+1):
    data = [[0]*15 for i in range(5)]
    result = ''
    for i in range(5):
        string = list(map(str,input()))
        for j in range(len(string)):
            data[i][j] = string[j]
    for x in range(15):
        for y in range(5):
            if data[y][x] == 0:
                result += ""
                continue
            else:
                result += data[y][x]
    print("#{} {}".format(t,result))