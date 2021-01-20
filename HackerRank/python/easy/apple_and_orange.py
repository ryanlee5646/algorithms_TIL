import math
import os
import random
import re
import sys


sys.stdin = open("input/apple_and_orange.txt","r")

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_cnt = 0
    orange_cnt = 0

    for apple in apples:
        if t >= (a + apple) >= s:
           apple_cnt +=1
    for orange in oranges:
        if t >= (b + orange) >= s:
           orange_cnt +=1
    print(apple_cnt)
    print(orange_cnt)


if __name__ == '__main__':
    # 집의 시작과 끝 좌표
    st = input().split()
    s = int(st[0])

    t = int(st[1])

    # a:사과나무 좌표, b: 오렌지나무 좌표
    ab = input().split()
    a = int(ab[0])

    b = int(ab[1])

    # m: 사과 좌표수, 오렌지 좌표수
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)
