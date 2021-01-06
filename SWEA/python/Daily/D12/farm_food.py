import sys
sys.stdin = open("farm_food.txt", "r")

T = int(input())

for t in range(1,T+1):
    N = int(input())
    Mymap = []
    farm = 0
    for i in range(N):
        data = list(map(int, input()))
        Mymap.append(data)
 
    for i in range((N//2)+1):
        farm += sum(Mymap[i][N//2-i:(N//2)+1+i])
   
    for j in range(N-(N//2),N): #(3,5)
        farm += sum(Mymap[j][(j-(N//2)):N-(j-(N//2))])
    print("#{} {}".format(t, farm))