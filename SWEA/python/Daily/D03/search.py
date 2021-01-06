Data = [4, 9, 11, 23, 2, 19, 7]

key = int(input())

# 순차 검색
for i in range(int(len(Data))):
    if key == Data[i]:
        print(i)
        break
else:
    print(False)



def binarySearch(Data, key):
    start = 0
    end = len(Data) -1
    while start <= end :
        middle = (start + end) // 2
        if Data[middle] == key:
            return True
        elif Data[middle] > key:
            end = middle -1
        else:
            start = middle + 1
    return False

print(binarySearch([4, 9, 11, 23, 2, 19, 7], 4))