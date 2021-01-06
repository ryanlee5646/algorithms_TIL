data = [38, 27, 43, 3, 9, 82, 10]

# def merge_sort(data):
#     if len(data)<=1:
#         return data
#     left = merge_sort(data[:len(data)//2])
#     right = merge_sort(data[len(data)//2:])
#     print("left: {}".format(left))
#     print("right: {}".format(right))
#     return merge(left, right)
#
# def merge(left, right):
#     result = [0]*len(data)
#     i=j=k= 0
#     while len(left) > i and len(right) > j:
#         if left[i] <= right[j]:
#             result[k] = left[i]
#             i+=1
#             k+=1
#         else:
#             result[k] = right[j]
#             j+=1
#             k+=1
#     if i >= len(left): #i = 1, k = 1, j =0
#         result[k:] = right[j:]
#     elif j >= len(right):
#         result[k:] = left[i:]
#     print("result: {}".format(result))
#     return result
# print(merge_sort(data))

def merge_sort(data):
    if len(data)<=1:
        return data
    left = merge_sort(data[:len(data)//2])
    right = merge_sort(data[len(data)//2:])

    print("left: {}".format(left))
    print("right: {}".format(right))
    return merge(left, right)

def merge(left, right):
    result = [0]*len(data)
    i=j=k= 0
    while len(left) > i and len(right) > j:
        if left[i] > right[j]:
            result[k] = left[i]
            i+=1
            k+=1
        else:
            result[k] = right[j]
            j+=1
            k+=1
    if i >= len(left): #i = 1, k = 1, j =0
        result[k:] = right[j:]
    elif j >= len(right):
        result[k:] = left[i:]
    print("result: {}".format(result))
    return result
print(merge_sort(data))