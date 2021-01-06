def Subset(here):
    if len(subset) == len(data):
        if sum(subset) == 0:
            print(subset)
        return
    if sum(subset) == 0:
        print(subset)

    for i in range(here, len(data)):
        if not visited[i]:
            visited[i] = 1
            subset.append(data[i])
            Subset(i)
            visited[i] = 0
            subset.pop()

data = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
visited = [0] * len(data)
n = len(data)
subset = []

Subset(0)


# def Subset(here):
#     if len(subset) == len(data):
#         # if sum(subset) == 0:
#         print(subset)
#         return
#     if len(subset) >= 0:
#         print(subset)
#
#     for i in range(here, len(data)):
#         if not visited[i]:
#             visited[i] = 1
#             subset.append(data[i])
#             Subset(i)
#             visited[i] = 0
#             subset.pop()
#
# data = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
# visited = [0] * len(data)
# n = len(data)
# subset = []
#
# Subset(0)

# for i in range(0, 1<<n):
#     for j in range(0,n):
#         if i & (1<<j):
#             subset_sum.append(data[j])
#     if sum(subset_sum) == 0:
#         subset.append(subset_sum)
#     subset_sum = []
# print(subset)
