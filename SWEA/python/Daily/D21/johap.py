


## JOHAP

checker=[0]*5
A=[0]*3
def go(now_index):

    if now_index==3:
        print(A)
        return

    for i in range(0,5):
        if checker[i]==0:
            if now_index>0:
                if A[now_index-1]>i:
                    continue
            checker[i]=1
            A[now_index]=i
            go(now_index+1)
            checker[i]=0

go(0)