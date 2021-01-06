# 0, 4, 1, 3, 1, 2, 4, 1

Data = list(map(int, input().split()))
Counts = [0] * (max(Data)+1)
Temp = [0] * (len(Data))

for index in Data:
    Counts[index] += 1
print(Counts)
for i in range(1, len(Counts)):
    Counts[i] += Counts[i-1]
print(Counts)
# Data = [0, 4, 1, 3, 1, 2, 4, 1]
# Counts = [1, 4, 5, 6, 8] < 누적시킨 카운트

for data in Data:
    Counts[data] -= 1 # 정렬된 카운터에서 중복된 숫자가 들어올때 index가 겹치지 않도록 감소
    Temp[Counts[data]] = data
print(Temp)