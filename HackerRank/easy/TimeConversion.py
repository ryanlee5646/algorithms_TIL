#!/bin/python3

import os
import sys

sys.stdin = open("input/TimeConversion.txt", "r")
#
# Complete the timeConversion function below.
#
def timeConversion(s):
    # Time Flag(AM/PM)
    flag = s[-2:]
    hh, mm, ss = [int(i) for i in s[:8].split(":")]
    if flag == 'PM':
        if hh == 12:
            hh = 12
        else:
            hh += 12
    else:
        if hh % 12 == 0:
            hh = 0
    return f'{hh:02}:{mm:02}:{ss:02}'

if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    print(result)
    # f.write(result + '\n')

    # f.close()
