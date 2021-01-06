import sys
sys.stdin = open("move_container.txt", "r")



T = int(input())

for t in range(1, T+1):
    container, truck = map(int, input().split())
    print("컨테이너수: {}".format(container))
    print("트럭수: {}".format(truck))
    cargo = list(reversed(sorted(map(int, input().split()))))
    truck_weight = list(reversed(sorted(map(int, input().split()))))
    print("트럭무게: {}".format(truck_weight))
    print("화물무게: {}".format(cargo))
    result = 0
    i = 0
    j = 0
    if container > truck:
        while i < truck: #컨테이너 수가 더 큰 경우 컨테이너 인덱스만 늘려서 비교
            if truck_weight[i] >= cargo[j]:
                result+=cargo[j]
                i+=1
                j+=1
            else:
                i+=1
    elif container <= truck: # 트럭의 수가 더 큰 경우 트럭 인덱스만 늘려서 비교
        while j < container:
            if truck_weight[i] >= cargo[j]:
                result+=cargo[j]
                i+=1
                j+=1
            else:
                j+=1
    elif result == 0: # 다 돌거나, 조건이 안맞는경우에 result가 증가하지 않아서 0이면 0을 출력
        print("#{t} 0")
    print("#{} {}".format(t,result))