import sys
sys.stdin = open("merge_sort.txt", "r")

def merge_sort(data):
    global count
    if len(data) <= 1:
        return data
    left = merge_sort(data[:len(data)//2])
    right = merge_sort(data[len(data)//2:])
    if left[-1] > right[-1]:
        count+=1
    return merge(left,right)

def merge(left, right):
    result = []
    i=j=k= 0
    while len(left) > i and len(right) > j:
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
            k+=1
        else:
            result.append(right[j])
            j+=1
            k+=1
    if i >= len(left): #i = 1, k = 1, j =0
        result[k:] = right[j:]
    elif j >= len(right):
        result[k:] = left[i:]
    return result

T = int(input())
for t in range(1,T+1):
    N = int(input())
    data = list(map(int,input().split()))
    count = 0
    result = merge_sort(data)
    print("#{} {} {}".format(t,result[len(result)//2],count))
