import sys
sys.stdin = open("input.txt","r")

def DFS(depth, sumScore, sumCal):
    global maxScore
    if depth == materialNum:
        if sumScore > maxScore and sumCal <= limitCal:
            maxScore = sumScore
        return
    if sumCal > limitCal:
        return
    if sumScore > maxScore and sumCal <= limitCal:
        maxScore = sumScore
    DFS(depth+1,sumScore + scoreData[depth], sumCal + calData[depth])
    DFS(depth+1,sumScore, sumCal)

T = int(input())
for t in range(1, T+1):
    materialNum, limitCal = map(int, input().split())
    scoreData = [0] * materialNum
    calData = [0] * materialNum

    for i in range(materialNum):
        scoreData[i],calData[i] = map(int,input().split())
    maxScore = 0
    DFS(0,0,0)

    print(f"#{t} {maxScore}")







