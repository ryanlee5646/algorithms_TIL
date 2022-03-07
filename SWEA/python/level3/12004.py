# leve3 구구단
from sys import stdin
input = stdin.readline

T = int(input())

# array = [False] * 101 # 왜 100으로 하면 안되지? N범위가 100인데?
# for i in range(1, 10):
#         for j in range(i, 10):
#             array[i*j] = True

# for t in range(1, T+1):
#     num = int(input())
#     if array[num] == True:
#         print(f"#{t} Yes")
#     else:
#         print(f"#{t} No")


for t in range(1, T+1):
    num = int(input())
    flag = True
    for i in range(1, 10):
        for j in range(i, 10):
            if (i*j) == num:
                print(f"#{t} Yes")
                flag = False
                break
        if(flag == False):
            break
    else:
        print(f"#{t} No")
    