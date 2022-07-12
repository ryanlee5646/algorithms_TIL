from sys import stdin
input = stdin.readline

# 접근 가능한지 체크
def is_possible(y, x):
  if (0 <= x < m) and (0 <= y < n) and not visit[y][x] and graph[y][x] == '.':
    return True
  return False

def pipe(y, x): 
  if x == m-1:
    return True
  
  for i in range(3):
    nx = x + dx[i]
    ny = y + dy[i]
    # DFS
    if is_possible(ny, nx):
      visit[ny][nx] = True
      if pipe(ny, nx):
        return True
  return False
  
n, m = map(int, input().split())
graph = [input().rstrip() for _ in range(n)]  # rstrip()을 이용해서 개행문자 제거
visit = [[0]*m for _ in range(n)]
count = 0
dx = [1, 1, 1]
dy = [-1, 0, 1]

for y in range(n):
  if pipe(y, 0):
    count += 1

print(count)
