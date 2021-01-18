import math
import os
import random
import re
import sys


# Complete the staircase function below.

sys.stdin = open("input/staircase.txt", "r")

# def staircase(n):
#
#     for i in range(n-1,-1,-1):
#         lst = []
#         for j in range(0,i):
#             lst.append(' ')
#         for k in range(n-i):
#             lst.append('#')
#         print(''.join(lst))

def staircase(n):

    for i in range(1, n+1):
        print(str('#'*i).rjust(n))

if __name__ == '__main__':
    n = int(input())

    staircase(n)


