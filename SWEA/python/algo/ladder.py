import sys
sys.stdin = open("input.txt", "r")

def IsSafe(y,x):
    if x >= 0 and x < 100 and y >= 0 and y < 100:
        return True
    else:
        return False


MyMap = [[0]*100 for i in range(100)]

T = int(input())
ladder = []
for i in range(100):
    Data = list(map(int, input().split()))
    ladder.append(Data)


dy = [0, 0, 1] # 사다리 아래로 이동
dx = [-1, 1, 0] # 사다리 좌우로 이동

res_index_x = 0
res_index_y = 99
for i in range(100):
    if ladder[99][i] == 2:
        res_index_x=i
for y in range(98,0,-1):
    if Data[y][res_index_x] == 1:
        res_index_y -= 1
    elif Data[y][res_index_x] == 1:
        res_index

print(res_index_x)