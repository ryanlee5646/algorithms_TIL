import sys
sys.stdin = open("GNS.txt", "r")

T = int(input())
dic = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, 
"FIV": 5 , "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9 }
reverse_dic= {0:'ZRO',1:'ONE',2:'TWO',3:'THR',4:'FOR',
5:'FIV',6:'SIX',7:'SVN',8:'EGT',9:'NIN'}

for t in range(1,T+1):
    print(t)
    tc, a = map(str,input().split())
    Data = list(map(str,input().split()))
    temp = []
    result = []
    for i in Data:
        temp.append(dic[i])
    temp.sort()
    print(temp)
    for j in temp:
        result.append(reverse_dic[j])
    print(len(result))
    # print("{}".format(tc))
    # print(' '.join(result))


