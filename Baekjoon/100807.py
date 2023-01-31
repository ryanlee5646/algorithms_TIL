# 개수 세기

from sys import stdin

input = stdin.readline

N = int(input())

arr = list(map(int, input().split()))

v = int(input())

print(arr.count(v))