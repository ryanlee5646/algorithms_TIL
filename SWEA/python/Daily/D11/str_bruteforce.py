import sys
sys.stdin = open("str.txt", "r")

T = int(input())
for t in range(1,T+1):
    flag = False
    pattern = input()
    target = input()
    j = 0
    i = 0
    count = 0
    while j < len(target):
        if pattern[i] != target[j]:
            j+=1
            i=0
            count = 0
        else:
            i+=1
            j+=1
            count += 1 
            if count == len(pattern):
                flag = True
                break
    if flag == True:
        print("#%d 1" % t)
    else:
        print("#%d 0" % t)

        