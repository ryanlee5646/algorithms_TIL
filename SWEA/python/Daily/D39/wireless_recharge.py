import sys
sys.stdin = open("wireless_recharge.txt", "r")

# 델타 방향이 총 5개
# 충전 범위 좌표를 리스트로 만드는거
# 저장값을 계속 누적, 도중에 가는데 더 적으면 리턴?
# 중복된 지점에 있으면 충전량 반으로 나눔


dy = [0, -1, 0, 1, 0] # 제자리, 상, 우, 하, 좌
dx = [0, 0, 1, 0, -1]

T = int(input())
for t in range(1,T+1):
    Time, N = map(int,input().split()) # time: 총시간, N = 충천기 수
    dir_A = list(map(int,input().split())) # 사람 A 이동 방향
    dir_B = list(map(int,input().split())) # 사람 B 이동 방향
    Ay,Ax = 0,0 # 사람 A 출발지점(좌표값을 1씩 낮춤)
    By,Bx = 9,9 # 사람 B 출발지점

    charger = []
    for i in range(N):
        x,y,r,p = map(int,input().split()) # 충전기 x,y좌표 r:범위, p: 충전량
        x-=1 # 배열의 값은 0부터 시작이므로 x,y 를 1씩 빼줌
        y-=1
        charger.append((y,x,r,p)) # 입력좌표를 y,x 로 바꿔서 튜플로 묶음
    charger.sort(key = lambda x:x[3], reverse=True) # power가 강한 충전기 순으로 정렬
    print(charger)

    time = 0 # while문 종료조건 time 횟수
    result = 0 # 결과값

    while True:
        print("time: {}".format(time))
        cntA = [0]*N # 각각 충전기 마다 A가 충전한 횟수
        cntB = [0]*N # 각각 충전기 마다 B가 충전한 횟수

        for i in range(N): #(y,x,r,p) 충전기 x[0],y[1]좌표 r[2]:범위, p[3]: 충전량
            if abs(Ay-charger[i][0]) + abs(Ax-charger[i][1]) <= charger[i][2]:
                cntA[i] += 1
                print("cntA{}".format(cntA))
            if abs(By-charger[i][0]) + abs(Bx-charger[i][1]) <= charger[i][2]:
                cntB[i] += 1
                print("cntB{}".format(cntB))
        check = 0
        A = 0
        B = 0
        for j in range(N):
            if not A and cntA[j] and not cntB[j]:
                result += charger[j][3]
                A+=1
                print("A:{}".format(A))
                print("result: {}".format(result))
            if not B and cntB[j] and not cntA[j]:
                result += charger[j][3]
                B+=1
                print("B:{}".format(B))
                print("result: {}".format(result))
            if cntA[j] and cntB[j]: # 같은 충전기를 공유하고있다면 2배가 아닌 그냥 기존 값을 올려줌 그리고 다음 충전기랑 걸쳐있다면 그 위치에서 더 증가시켜줌
                result += charger[j][3]
                check+=1
                print("check:{}".format(check))
                print("result: {}".format(result))
            if A+B+check >= 2:
                break
        if time>= Time:
            break
        Ay += dy[dir_A[time]]
        Ax += dx[dir_A[time]]
        By += dy[dir_B[time]]
        Bx += dx[dir_B[time]]
        time+=1

        print()
    print("#{} {}".format(t,result))