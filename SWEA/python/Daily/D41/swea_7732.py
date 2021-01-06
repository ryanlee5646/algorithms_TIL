import sys

sys.stdin = open("swea_7782.txt", "r")

T = int(input())

for t in range(1,T+1):
    now = input()
    promise = input()
    nowT, nowM, nowS = int(now[:2]), int(now[3:5]), int(now[6:])
    promiseT, promiseM, promiseS = int(promise[:2]), int(promise[3:5]), int(promise[6:])
    resultT = resultM = resultS = 0
    result = ''

    if int(nowT) > int(promiseT) :
        promiseT = int(promiseT) + 24
    if int(nowM) > int(promiseM):
        promiseT -= 1
        promiseM = int(promiseM) + 60
    if int(nowS) > int(promiseS):
        promiseM -=1
        promiseS = int(promiseS) + 60

    resultT = int(promiseT) - int(nowT)
    resultM = int(promiseM) - int(nowM)
    resultS = int(promiseS) - int(nowS)
    if resultT < 10:
        result += '0'+str(resultT)+':'
    else:
        result += str(resultT) + ':'
    if resultM < 10:
        result += '0' + str(resultM) + ":"
    else:
        result += str(resultM) + ":"
    if resultS < 10:
        result += '0' + str(resultS)
    else:
        result += str(resultS)

    print("#{} {}".format(t,result))
