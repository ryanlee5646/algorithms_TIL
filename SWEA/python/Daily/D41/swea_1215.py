import sys
sys.stdin = open("swea_1215.txt","r")

def IsSafe(y,x):
    if 0<=y<8 and 0<=x<8:
        return True
    else:
        return False


def word(sy,sx):
    global result
    garo = ''
    sero = ''

    if IsSafe(sy, sx+length): # 가로 검토
        ny, nx = sy, sx+length
        for x in range(sx,nx):
            garo += data[ny][x]

        if garo[0:len(garo)//2] == garo[-1:-len(garo)//2- 1:-1]:
            print(garo)
            result += 1

    if IsSafe(sy+length, sx): # 세로 검토
        ny, nx = sy+length, sx
        for y in range(sy,ny):
            sero += data[y][nx]
        if sero[0:len(sero) // 2] == sero[-1:-len(sero)//2 - 1:-1]:
            print(sero)
            result += 1


T = int(input())
for t in range(1,T+1):
    length = int(input())
    data = [input() for _ in range(8)]
    result = 0


    for y in range(8):
        for x in range(8):
            word(y,x)

    print("#{} {}".format(t,result))