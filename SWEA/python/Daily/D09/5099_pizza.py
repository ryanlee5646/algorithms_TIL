import sys
sys.stdin = open("5099_pizza.txt", "r")

T = int(input())

for t in range(1,T+1):
    oven, pizza = map(int, input().split())
    cheese = list(map(int, input().split()))
    num_cheese = [] #치즈 양
    pizza_num = [] # 피자 번호
    Queue = [] # 화덕
    for i in range(1, pizza+1):
        pizza_num.append(i)
    pizza_cheese = list(map(list, zip(pizza_num, cheese)))  # 피자 번호하고 치즈양을 리스트로 묶음
    print(pizza_cheese)
    
    for j in range(oven):
        Queue.append(pizza_cheese.pop(0))

    while len(Queue) > 1: # 피자가 하나 남을때 까지 반복
        if Queue[0][1] //2 != 0: # 첫번째 피자의 치즈가 0이 아니라면 
            Queue[0][1] = Queue[0][1] // 2 # 화덕에서 먼저 치즈 감소 시키고
            a = Queue.pop(0) # 잠시 빼낸 피자를 변수에 저장하고
            Queue.append(a) # 다시 화덕 맨뒤로 append
            
        elif Queue[0][1] == 0: # 화덕 첫번째 피자의 치즈가 0이라면
            Queue.pop(0) # 꺼냄
            if len(pizza_cheese) > 0: # 그리고 피자 리스트에 남아 있는(아직 굽지않은) 피자를 앞에꺼부터 추가해주는데 
                Queue.append(pizza_cheese.pop(0))
            else: # 남은 피자가 없으면 그냥 패스함
                pass
        
    print(f'#{t} {Queue[0][0]}')


    
    



    

    # 한번 돌릴때마다 첫번째 인덱스에 오는 피자의 치즈가 0인지 확인
    #아니면 계속 회전시키고 화덕 개수만큼 돌렷을때 //2 해주기
