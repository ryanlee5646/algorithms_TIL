# leve3 구구단
from sys import stdin
input = stdin.readline

def combination(depth):
    global count
    if count > 0:
        print(f"#{t} Yes")
        return
    if depth == 2:    
        if (tmp[0] * tmp[1]) == num:
            count+=1
    
    for i in range(depth, len(num_list)):
        tmp.append(num_list[i])
        combination(depth+1)
        tmp.pop()
        
T = int(input())

for t in range(1, T+1):
    num = int(input())
    num_list = [1,2,3,4,5,6,7,8,9]
    tmp = []
    count = 0
    combination(0)
    if count == 0:
        print(f"#{t} No")
    # else: 
    #     print(f"#{t} Yes")