import sys
sys.stdin = open("computer_worm_2606.txt", "r")

def find_set(x): #부모가 자기자신인지 찾고 아니라면 부모를 찾아줌

    if x == p[x]:
        return x
    else:
        return find_set(p[x])

def union(x,y): #y자리에 부모를 이어줌
    p[find_set(y)] = find_set(x)


computer = int(input())
p = [0]*(computer+1)
N = int(input())
count = 0

for i in range(1, computer+1):  #자기 자신이 부모가 되게 이어줌
    p[i] = i

for j in range(N):
    road = list(map(int,input().split()))
    union(road[0],road[1])

# print(p)
for i in range(1,computer+1): # 1번컴퓨터랑 나머지의 부모가 같은지 확인
    if find_set(p[1]) == find_set(p[i]):
        count+=1

print(count-1)
