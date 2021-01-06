import sys, itertools
sys.stdin = open("lab.txt","r")

def Issafe(y,x):
	if 0<=y<N and 0<=x<N and data[y][x] != 1:
		return True
	else:
		return False

def DFS(start):
	global possible, low
	queue = start

	temp = 0
	for i in start:
		visited[i[0]][i[1]] = 0 # 시작지점은 시간을 0을 찍음
	while start:
		y,x = queue.pop(0)
		for dir in range(4):
			ny = y+dy[dir]
			nx = x+dx[dir]
			if Issafe(ny,nx):
				if visited[y][x] + 1 < visited[ny][nx]:
					visited[ny][nx] = visited[y][x] + 1
					queue.append([ny,nx])
	for y in range(N):
		for x in range(N):
			if visited[y][x] != 0 and visited[y][x] != 987654321:
				temp+=1
	if temp == room:
		temp1 = 0
		for y in range(N):
			for x in range(N):
				if visited[y][x] != 987654321:
					if visited[y][x] > temp1:
						temp1 = visited[y][x]
		if temp1 < low:
			low = temp1
			possible += 1
dy = [-1,1,0,0]
dx = [0,0,-1,1]
N, M = map(int,input().split())
data = [list(map(int,input().split()))for _ in range(N)]
start = [] # 가능한 시작지점 좌표
room = 0
possible = 0
low = 987654321
for y in range(N):
	for x in range(N):
		if data[y][x] == 2:
			start.append([y,x])
		if data[y][x] == 0:
			room += 1
# 바이러스가 퍼진 공간이 room 수만큼 되야함
room = room + len(start) - M # 숫자가 0인 빈칸 + 바이러스 M개의 시작점을 제외한  남은 바이러스 칸수

combination = list(itertools.combinations(start,M))
for i in combination:
	visited = [[987654321] * N for _ in range(N)]
	# print(i)
	DFS(list(i))
if possible == 0:
	print("-1")
else:
	print(low)

