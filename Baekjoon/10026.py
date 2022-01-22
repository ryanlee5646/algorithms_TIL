# 적록색약

from collections import deque

def bfs(x, y):
    queue.append([x, y])
    visit[x][y] = cnt
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if data[nx][ny] == data[x][y] and visit[nx][ny] == 0:
                    queue.append([nx, ny])
                    visit[nx][ny] = 1

N = int(input())
data = [list(map(str, input()) for _ in range(N))]
visit = [[0]*N for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()

# 일반사람
cnt = 0
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt, end=' ')

# 적록색맹
for i in range(N):
    for j in range(N):
        if data[i][j] == 'R':
            data[i][j] = 'G'
            
visit = [[0]*N for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt)

