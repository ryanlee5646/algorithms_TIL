import sys

sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용

Data = list(map(int, input().split()))

print(Data)

#Gravity(낙차) 알고리즘
max_height = 0
for now in range(len(Data)):
    num = Data[now]
    height = 0
    for Next in range(now+1, len(Data)):
        if num > Data[Next]:
            height += 1
        else:
            height += 0
    if height > max_height:
        max_height = height
print(max_height)
#

# for now in range(size):
#     jumpcnt = size-now-1