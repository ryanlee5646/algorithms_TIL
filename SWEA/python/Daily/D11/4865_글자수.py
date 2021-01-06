import sys
sys.stdin = open("4865_글자수.txt", "r")

T = int(input())

for t in range(1,T+1):
    word = input()
    string = input()
    result =[]
    for i in word:
        count = 0
        for j in string:
            if i == j:
                count+=1
        result.append(count)
    print("#{} {}".format(t,max(result)))
                