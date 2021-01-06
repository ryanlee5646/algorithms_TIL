import sys
sys.stdin = open("5185_bi_num.txt","r")

# 16진수 1자리는 2진수 4자리로 표시된다.
# N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 프로그램을 만드시오.
# 단, 2진수의 앞자리 0도 반드시 출력한다.
# 예를 들어 47FE라는 16진수를 2진수로 표시하면 다음과 같다.
# 0100011111111110

def GetSome(n,k):
    if n < k:
        result.append(n)
        return
    else:
        GetSome(n//k,k)
        result.append(n%k)

hex_list = {
    "A":10, "B":11, "C":12, "D":13, "E":14, "F":15
}

T = int(input())
for t in range(1,T+1):
    N, hex = input().split()
    dec_num = 0
    mul = 0
    result = []
    for i in reversed(hex):
        if mul == 0 and i in hex_list:
            dec_num+=hex_list[i]
            mul+=1
        elif mul != 0 and i in hex_list:
            dec_num+=hex_list[i]*(16**mul)
            mul+=1
        else:
            dec_num+= int(i)*(16**mul)
            mul+=1
    GetSome(dec_num,2)
    add = 0
    if len(result) % 4 != 0: #자리수 만큼 맨 앞에 0을 추가
        add = (((len(result)//4)+1)*4) - len(result)
    while add!=0:
        result.insert(0,0)
        add-=1
    print("#{} ".format(t), end='')
    print(*result,sep='')


