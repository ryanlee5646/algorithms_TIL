import sys
sys.stdin = open("recur_selection_sort.txt","r")

# 12 3 78 20 23 4

def Select(start, end):
    if start == end:
        return
    low = data[start]
    low_index = start
    for i in range(start, len(data)):
        if low>data[i]:
            low=data[i]
            low_index = i
    data[start],data[low_index] = data[low_index],data[start]
    return Select(start+1,end)


T = int(input())
for t in range(1, T+1):
    data = list(map(int, input().split()))
    Select(0, len(data)-1)
    print(data)