import sys
sys.stdin = open("4869.txt", "r")
#
# def Paper(g):
#     global count
#     if garo == 10:
#         count = 1
#         return
#     if garo == 20:
#         count = 3
#         return
#     if g == garo:
#         count+=1
#         return
#     if g > garo:
#         return
#     for i in range(3):
#         Paper(g+square_g[i])
#
# T = int(input())
# for t in range(1,T+1):
#     garo = int(input())
#     count = 0
#     visited = [0]*3
#     square_g = [20,10,20]
#     Paper(0)
#     print("#{} {}".format(t,count))

def Paper(garo):
    if garo == 10:
        return 1
    if garo == 20:
        return 3
    return Paper(garo-10) + Paper(garo-20)*2

T = int(input())
for t in range(1,T+1):
    garo = int(input())
    print("#{} {}".format(t,Paper(garo)))