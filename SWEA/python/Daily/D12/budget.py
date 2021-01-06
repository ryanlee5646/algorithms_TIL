import sys
sys.stdin = open("budget.txt", "r")

Budget = int(input()) #남은 예산
act_num = int(input()) #활동수
money = list(map(int, input().split()))
result = 0

def Max_Sum(start, cost):
    global result, money
    if cost > 40: return
    elif start == len(money):
        if cost > result:
            result = cost
        return

    elif start > len(money):
        return
        #     else:
        #         return
        # else:
        #     # temp = cost - money[start]
        #     # if result < temp:
        #     #     result = temp
        #     return

    Max_Sum(start+1,cost+money[start])
    Max_Sum(start+1,cost)


print(money)


Max_Sum(0,0)
print(result)