# N과 M (4) -조합(중복 숫자 인정)
from sys import stdin
input = stdin.readline

def combination(start):
    if len(tmp) == M:
        print(' '.join(map(str, tmp)))
        return
    
    for i in range(0, len(data)):
        # if not visited[i]:
        # 중복 체크 안하면됌
        #    visited[i] = 1
        # tmp 배열 마지막 값이 새로 추가될 값보다 크면 넣지않고 패스
        if len(tmp) > 0:
            if tmp[-1] > data[i]:
                continue
        tmp.append(data[i])
        combination(start+1)
        #    visited[i] = 0 # 끝까지 탐색 했으면 빼
        tmp.pop()
 
N, M = map(int, input().split())
data = [i for i in range(1, N+1)]
# visited = [0] * N
tmp = []
combination(0)
