# import sys
# sys.stdin = open("hex_to_deci.txt", "r")

data = '01D06079861D79F99F'
bi = ''
hex_num ={
    '0':'0000', '1':'0001','2':'0010', '3':'0011',
    '4':'0100', '5':'0101','6':'0110', '7':'0111',
    '8':'1000', '9':'1001','A':'1010', 'B':'1011',
    'C':'1100', 'D':'1101','E':'1110', 'F':'1111',
}
for i in data:
    bi+=hex_num[i]

num_list = []
print(bi)
for i in range(0,((len(bi)//7)-1)*7+1,7): #0부터 7씩 증가하는 시작점
    temp = []
    for j in range(i,i+7):
        temp.append(bi[j])
    num_list.append(temp)
temp = []
for l in range(((len(bi)//7)-1)*7+7,len(bi)):
    temp.append(bi[l])
num_list.append(temp)
print(num_list)

for k in num_list:
    sum = 0
    for l in range(len(k)):
        sum += int(k[len(k)-1-l])*2**l
    print(sum)

