import sys

# 2, 3, 5, 7, 11
sys.stdin = open("swea_1945.txt","r")

T = int(input())
for t in range(1, T+1):
    num = int(input())
    div = [2,3,5,7,11]
    result = [0]*5
    for i in range(len(div)):
        while True:
            if num % div[i] == 0:
                result[i]+=1
                num /= div[i]
            else:
                break
    print("#{}".format(t), *result)


