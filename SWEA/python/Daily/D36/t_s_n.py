import sys
sys.stdin = open("t_s_n.txt")

for i in range(1,int(input())+1):
    temp = ''
    for j in str(i):
        if j == '3' or j== '6' or j=='9':
            temp+='-'
        else:
            temp+=j
    if temp.count('-') == 1:
        print('-', end=' ')
    else:
        print(temp, end = ' ')