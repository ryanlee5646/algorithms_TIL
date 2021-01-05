#!/bin/python3

import math
import os
import random
import re
import sys
import time
start = time.time()

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#
sys.stdin = open("input/BirthdayCakeCandles.txt", "r")

# Solution 1
def birthdayCakeCandles(candles):
    arr = sorted(candles, reverse=True)
    count = arr.count(arr[0])
    return count

## Solution 2
# def birthdayCakeCandles(candles):
#     tallest_candle = 0
#     count = 0
#
#     for i in candles:
#         height = i
#         if(height > tallest_candle):
#             tallest_candle = height
#             count = 1
#         elif(height == tallest_candle):
#             count += 1
#     return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    print("time :", time.time() - start)
    # fptr.write(str(result) + '\n')

    # fptr.close()
