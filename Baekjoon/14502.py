# 연구소1
from sys import stdin
input = stdin.readline

tmp = []
def combination(start):
    if len(tmp) == 3:
        walls_position.append(tmp)
        return
    for i in (start, len(blanks)):
        if not visited[i]:
            visited[i] = 1
            tmp.append(blanks[i])
            combination(start+1)
            visited[i] = 0
            tmp.pop()
        
# 방향(상, 하, 좌, 우)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
blanks = []
walls_position = []
visited = [0] * len(walls_position)
# 벽을 세울 수 있는 자표
for y in range(N):
    for x in range(M):
        if data[y][x] == 0:
            blanks.append((y,x))
combination(0)

print(walls_position)