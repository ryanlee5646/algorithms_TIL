# import sys
# sys.stdin = open("password_pattern.txt","r")

data = '0269FAC9A0'
bi = ''
hex_num ={
    '0':'0000', '1':'0001','2':'0010', '3':'0011',
    '4':'0100', '5':'0101','6':'0110', '7':'0111',
    '8':'1000', '9':'1001','A':'1010', 'B':'1011',
    'C':'1100', 'D':'1101','E':'1110', 'F':'1111',
}
password = {
    '001101':0, '010011':1, '111011':2, '110001':3,
    '100011':4, '110111':5, '001011':6, '111101':7,
    '011001':8, '101111':9
}
for i in data:
    bi+=hex_num[i]
i = -1
while bi[i] == '0':
    i-=1
stack = []
for j in range(i,0-len(bi)-1,-6):
    if len(bi[j-5:j+1]) == 6:
        stack.append(password[bi[j-5:j+1]])
for i in range(len(stack)):
    print(stack.pop(-1), end=' ')


