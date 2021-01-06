import sys
sys.stdin = open("quick_ex03.txt","r")

def Partition(data, L, R):
    p = data[L]
    i = L
    j = R

    while i < j:
        while data[i] <= p and i < R:
            i+=1
            print('i', i)
        while data[j] >= p and j > L :
            j-=1
            print('j', j)
        if i < j:
            data[i], data[j] = data[j], data[i]
            print(data)
    data[L], data[j] = data[j], data[L]
    return j
def Quick(data,L,R):
    if L < R:
        s = Partition(data,L,R)
        Quick(data,L,s-1)
        Quick(data,s+1,R)


T = int(input())
for t in range(1,T+1):
    data = list(map(int,input().split()))
    print(data)
    Quick(data,0,len(data)-1)
    print(data)
