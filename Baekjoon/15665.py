# N과 M(11)
from sys import stdin
input = stdin.readline

def permutaion(start):
    if start == M:
        check = ' '.join(map(str, tmp))
        if check not in dic:
            dic[check] = 1
            print(check)
        return
    for i in range(len(data)):
        tmp.append(data[i])
        permutaion(start+1)
        tmp.pop()
        
N, M = map(int, input().split())
data = sorted(list(map(int, input().split())))
tmp = []
dic = {}
permutaion(0)
