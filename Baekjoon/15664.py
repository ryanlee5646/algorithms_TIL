# N과 M(10)
from sys import stdin
input = stdin.readline

def combination(start):
    if len(tmp) == M:
        check = ' '.join(map(str, tmp))
        if check not in dic:
            dic[check] = 1
            print(check)
        return
    
    for i in range(start, len(data)):
        if not visited[i]:
            # 앞자리가 뒷자리 보다 크면 패스
            if len(tmp):
                if tmp[-1] > data[i]:
                    continue
            visited[i] = 1
            tmp.append(data[i])
            combination(start+1)
            visited[i] = 0
            tmp.pop()

N, M = map(int, input().split())
data = sorted(list(map(int, input().split())))
visited = [0] * N
tmp = []

dic = {}
combination(0)