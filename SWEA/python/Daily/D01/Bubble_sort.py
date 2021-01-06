# 버블 알고리즘

Data = list(map(int, input().split()))
# for now in range(len(Data)-1):
#     for next in range(now+1, len(Data)):
#         if Data[next] < Data[now]:
#             Data[now], Data[next] = Data[next], Data[now]
# print(Data)

# 7 16 1 77 54 3

for now in range(len(Data)-1):
    for next in range(now+1, len(Data)):
        if Data[now] > Data[next]:
            Data[now], Data[next] = Data[next], Data[now]
print(Data)