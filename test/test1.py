# tc1
money = 4578
costs = [1, 4, 99, 35, 50, 1000] # 1원, 5원, 10원, 50원, 100원, 500원

# tc2
# money = 1999
# costs = [2, 11, 20, 100, 200, 600]

def calcurator(remain, cost, depth): # 계산 하고 남은금액, 더한금액, 
    global money
    if remain == 0:
        print(cost)
        return 
    count = remain // coin_cost[depth][0] # 동전수
    remain -= coin_cost[depth][0] * count # 남은금액 계산
    cost += coin_cost[depth][1] * count # 최소비용 더하기  
    calcurator(remain, cost, depth+1)    

coins = [1, 5, 10, 50, 100, 500]

# 동전과 비용을 묶음
coin_cost = list(zip(coins, costs))

# 최소비용 기준으로 정렬함 ex) [(100, 50), (50, 35), (5, 4), (1, 1), (500, 1000), (10, 99)]
coin_cost.sort(key = lambda x : -(x[0]/x[1]))

calcurator(money, 0, 0)

