import sys
sys.stdin = open("jungsik_bank.txt","r")

T = int(input())

for t in range(1,T+1):
    two = list(map(int,(input())))
    three = list(map(int,(input())))
    bi_num = [two[:] for _ in range(len(two))]

    for i in range(len(two)): # 이진수 각 자리를 바꾼 이차원 리스트
        if bi_num[i][i] == 1:
            bi_num[i][i] = 0
        else:
            bi_num[i][i] = 1
    bi_to_dec = [] #이진수를 십진수를 변환하여 리스트에 담음
    for y in range(len(bi_num)):
        temp = 0
        i = len(bi_num)-1
        for x in range(len(bi_num)):
            temp+=bi_num[y][x]*2**i
            i-=1
        bi_to_dec.append(temp)

    th_num = [] # 3진수 각자리에 경우의 수를 바꿈
    for k in range(len(three)):
        temp1 = three[:]
        temp2 = three[:]
        if temp1[k] == 0 and temp2[k] == 0:
            temp1[k] += 1
            temp2[k] += 2
            th_num.append(temp1)
            th_num.append(temp2)
        elif temp1[k] == 1 and temp2[k] == 1:
            temp1[k] -= 1
            temp2[k] += 1
            th_num.append(temp1)
            th_num.append(temp2)
        elif temp1[k] == 2 and temp2[k] == 2 :
            temp1[k] -= 1
            temp2[k] -= 2
            th_num.append(temp1)
            th_num.append(temp2)

    th_to_dec = []
    for y in range(len(three)*2):
        temp = 0
        i = len(three)-1 # 제곱할 수
        for x in range(len(three)):
            temp+=th_num[y][x]*3**i
            i-=1
        th_to_dec.append(temp)

    for z in th_to_dec:
        if z in bi_to_dec:
            print("#{} {}".format(t,z))


