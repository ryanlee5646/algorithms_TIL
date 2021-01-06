# import sys
# sys.stdin = open("segment_tree.txt", "r")

def update(a,b): #3번째를 1로
    where = base + a - 1
    IDT[where] = b
    where >>= 1
    while where:
        IDT[where] = IDT[where*2] + IDT[where*2+1]
        where >>= 1
        print(IDT)

def RSQ(ffrom, to): # 1부터 4까지 구하면
    ffrom = ffrom+base-1 #from 8이되고
    to = to + base -1# to는 11이됨
    sum = 0

    while ffrom < to:
        if ffrom%2==1 :
            sum += IDT[ffrom]
            ffrom+=1
        ffrom >>= 1 # 만약 ffrom이 짝수면 부모로 보냄
        if to % 2 == 0:
            sum += IDT[to]
            to-=1
        to>>=1 # 만약 to가 홀수면 부모로 보냄

    if ffrom == to:
        sum += IDT[ffrom]
    return sum
IDT = [0] * (1<<4)
Data = list(map(int, input().split()))
howmany = len(Data)
base = 1

while base < howmany:
    base <<=1
for now in range(base, howmany+base):
    IDT[now] = Data.pop(0)
#부모한테 합을 써줌(거꾸로 써준다 base-1 ~ 1번 방까지)
for parent in range(base-1, 0, -1):
    IDT[parent] = IDT[parent*2] + IDT[parent*2+1]

# print(IDT)
# update(3,1)
print(RSQ(2,8))


# update 세번째 있는 수자 1을 2로 바꿔 본다.