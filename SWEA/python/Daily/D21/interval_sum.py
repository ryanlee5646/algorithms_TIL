

data = [5, 1, -4, 2, -1, -5, -2, 8, -3, 6]
range_sum = [0] * len(data)
range_sum[0] = data[0]

high=high_index=0

for now in range(1,len(data)):
    if range_sum[now-1] + data[now] > data[now]:
        range_sum[now] = range_sum[now-1]+data[now]
    else:
        range_sum[now] = data[now]

    if range_sum[now] > high:
        high = range_sum[now]
        high_index = now
result = 0
for i in range(high_index,-1,-1):
    if result==high:
        break
    else:
        result+=data[i]
        print(data[i], end=" ")




# for now in range(1,len(data)):
#     range_sum[now] = max(range_sum[now-1] + data[now] , data[now])