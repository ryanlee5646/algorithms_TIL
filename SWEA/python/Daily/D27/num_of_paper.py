import sys
sys.stdin = open("num_of_paper.txt", "r")

def IsSame(y,x,size):
    for i in range(y,y+size):
        for j in range(x,x+size):
            if data[y][x] != data[i][j]:
                return False
    return True

def GetSome(y,x,size):
    global N_0, N_1, N_minus
    if IsSame(y,x,size):
        if data[y][x] == 0:
            N_0+=1
        elif data[y][x] == 1:
            N_1+=1
        else:
            N_minus+=1
    else:
        next = size // 3
        for i in range(3):
            for j in range(3):
                GetSome(y+i*next, x+j*next, next)

N = int(input())
data = []
N_0 = 0
N_1 = 0
N_minus = 0

for i in range(N):
    data.append(list(map(int,input().split())))
GetSome(0,0,N)
print(N_minus)
print(N_0)
print(N_1)
