import sys
from itertools import combinations
sys.stdin = open("castle_defence.txt", "r")

T = int(input())

for t in range(1,T+1):
    h, w, d = map(int,input().split())
    Mymap = [list(map(int,input().split())) for _ in range(h)] + [[0]*w]
    castle = [i for i in range(w)]