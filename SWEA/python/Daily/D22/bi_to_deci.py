import sys
sys.stdin = open("bi_to_deci.txt", "r")

data = list(map(int,input()))
num_list = []
for i in range(0,len(data),7):
    temp = []
    for j in range(i,i+7):
        temp.append(data[j])
    num_list.append(temp)

for k in num_list:
    sum = 0
    for l in range(7):
        sum += k[6-l]*2**l
    print(sum, end=" ")



# result = 0
# for i in range(len(data)):
#     temp = (1<<6)>>(i%7)
#
#     if temp&(data[i]<<6)>>(i%7):
#         result+=temp
#
#     if i%7==6:
#         print(result)
#         result = 0