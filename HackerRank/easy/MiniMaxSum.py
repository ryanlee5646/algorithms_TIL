#!/bin/python3

import math
import os
import random
import re
import sys
import time
start = time.time()
# READ input File
# sys.stdin = open('input/MiniMaxSum1.txt', 'r')
sys.stdin = open('input/MiniMaxSum2.txt', 'r')

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    minSum = 0
    maxSum = 0
    minSortArr = sorted(arr)
    maxSortArr = sorted(arr, reverse=True)

    for i in range(4):
        minSum += minSortArr[i]
        maxSum += maxSortArr[i]
    print(f"{minSum} {maxSum}")

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
    print("time :", time.time() - start)