data = [1, 9, 3, 2, 7, 0, 4]


# for i in range(1, len(data)):
#     result.append(data[i])
#     here = i
#     while True:
#         if here > 0 and result[i] > result[here-1]:
#             result[here-1] = result[here]
#             result[here] = result[here-1]
#             here -= 1
#         else:
#             break
#     print(result)


for i in range(1, len(data)):
    key = data[i]  # 비교당할 위치의 데이터
    j = i - 1
    print(key)
    while j>=0 and data[j] > key:
        data[j+1] = data[j]
        j -= 1
        print(data)

    data[j+1] = key

print(data)


