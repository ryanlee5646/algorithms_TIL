# x = [i for i in range(1,101)]
# y = [i for i in range(1,101)]
# z = [i for i in range(1,101)]
# count = 0
# for i in x:
#     for j in y:
#         for k in z:
#             if i+j+k == 100 and i<=j<=k:
#                 count+=1
#                 print(i, j, k, sep=' ')
# print(count)

def xyz(x,y,z):
    global count
    if x+y+z > 100:
        return
    if x>y or y > z:
        return
    if x+y+z == 100:
        print(x, y, z, sep=' ')
        count += 1
        return
    if visited[x+1][y][z] == False:
        visited[x+1][y][z] = True
        xyz(x+1,y,z)
    if visited[x][y+1][z] == False:
        visited[x][y+1][z] = True
        xyz(x, y+1, z)
    if visited[x][y][z+1] == False:
        visited[x][y][z+1] = True
        xyz(x,y,z+1)


visited = [[[0]*100 for _ in range(100)]for j in range(100)]
count = 0
xyz(1,1,1)
print(count)
# for i in x:
#     for j in y:
#         for k in z:
#             GetSome(i,j,k)