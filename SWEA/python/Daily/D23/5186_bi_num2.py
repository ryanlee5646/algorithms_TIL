import sys
sys.stdin = open("5186_bi_num2.txt","r")

T = int(input())

for t in range(1,T+1):
    div = 0.5
    result = ''
    data = float(input())
    i = 0
    while i < 13:
        if data - div > 0:
            data -= div
            i+=1
            div/=2
            result+='1'
        elif data - div < 0:
            i+=1
            div/=2
            result+='0'
        else:
            result+='1'
            break
    if len(result) > 12:
        print("#{} overflow".format(t))
    else:
        print("#{} {}".format(t,result))

