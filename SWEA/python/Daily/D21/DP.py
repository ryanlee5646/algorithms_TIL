data=[5,1,-4,2,-1,-5,-2,8,-3,6]

rangesum=[0]*len(data)
rangesum[0]=data[0]

high=high_index=0
for now in range(1,len(data)):
    rangesum[now]=max(rangesum[now-1]+data[now],data[now])
    if rangesum[now]>high:
        high=rangesum[now]
        high_index=now

print(high)
result=0
for i in range(high_index,-1,-1):
    if result==high:
        break
    else:
        result+=data[i]
        print(data[i],end=" ")