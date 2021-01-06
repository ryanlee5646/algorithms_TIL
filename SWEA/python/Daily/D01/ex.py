import sys

sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용

Data = list(map(int, input().split()))

Max = Data[0]
Max_index = -1
for i in range(len(Data)):
    if Max < Data[i]:
        Max = Data[i]
        Max_index = i

print(Max, Max_index)