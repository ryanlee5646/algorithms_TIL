import sys
sys.stdin = open("baby_gin.txt", "r")

def babygin():
    for i in range(len(gin)):
        if gin[i][0] == gin[i][1] == gin[i][2] and gin[i][3] == gin[i][4] == gin[i][5]:
            print("babygin!")
            break
        elif (gin[i][1] == gin[i][0]+1 and gin[i][1] == gin[i][2]-1) and (gin[i][4] == gin[i][3]+1 and gin[i][4] == gin[i][5]-1):
            print("babygin!")
            break
        elif (gin[i][1] == gin[i][0]-1 and gin[i][1] == gin[i][2]+1) and gin[i][3] == gin[i][4] == gin[i][5]:
            print("babygin!")
            break
    else:
        print("not babygin!")


T = int(input())
for t in range(1,T+1):
    data = list(map(int,input().split()))
    print(data)
    gin = []
    for a in range(len(data)):
        for b in range(len(data)):
            if a!= b:
                for c in range(len(data)):
                    if a!=c and b!=c:
                        for d in range(len(data)):
                            if a!=d and b!=d and c!=d :
                                for e in range(len(data)):
                                    if a!=e and b!=e and c!=e and d!=e:
                                        for f in range(len(data)):
                                            if a!=f and b!=f and c!=f and d!=f and e!=f:
                                                gin.append([data[a],data[b],data[c],data[d],data[e],data[f]])
    babygin()


