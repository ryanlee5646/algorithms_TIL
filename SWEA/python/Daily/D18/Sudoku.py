import sys
sys.stdin = open("Sudoku.txt","r")


def garo():
    global flag
    for y in range(9):
        count = [1] + [0] * 9
        for x in range(9):
            count[data[y][x]] = 1
        if 0 in count:
            flag = False
            return
def sero():
    global flag
    for x in range(9):
        count = [1] + [0] * 9
        for y in range(9):
            count[data[y][x]] = 1
        if 0 in count:
            flag = False
            return
def square():
    global flag
    for y in range(0, 9, 3):
        for x in range(0, 9, 3):
            count = [1] + [0] * 9
            for i in range(3):
                for j in range(3):
                    count[data[y + i][x + j]] = 1
            if 0 in count:
                flag = False
                return

T = int(input())
for t in range(1, T + 1):
    data = []
    flag = True
    for i in range(9):
        data.append(list(map(int, input().split())))
    garo()
    sero()
    square()

    if flag:
        print("#{} 1 ".format(t))
    else:
        print("#{} 0".format(t))
