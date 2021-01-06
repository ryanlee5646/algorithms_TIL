import sys
sys.stdin = open("snail.txt","r")

T = int(input())

def IsSafe(y,x):
	if 0<=y<N and 0<=x<N:
		return True
	else:
		return False

def DFS(y,x,flag,num):
	if num == N**2:
		data[y][x] = num
		return
	if flag == 'right':
		if IsSafe(y+dy[0],x+dx[0]) and data[y+dy[0]][x+dx[0]] == 0:
			data[y+dy[0]][x+dx[0]] = num+1
			DFS(y+dy[0], x+dx[0], flag, num+1)
		else:
			flag = 'down'
			DFS(y,x,flag,num)
	elif flag == 'down':
		if IsSafe(y+dy[1],x+dx[1]) and data[y+dy[1]][x+dx[1]] == 0:
			data[y+dy[1]][x+dx[1]] = num+1
			DFS(y+dy[1], x+dx[1], flag, num+1)
		else:
			flag = 'left'
			DFS(y, x, flag, num)
	elif flag == 'left':
		if IsSafe(y+dy[2],x+dx[2]) and data[y+dy[2]][x+dx[2]] == 0:
			data[y+dy[2]][x+dx[2]] = num+1
			DFS(y+dy[2], x+dx[2], flag, num+1)
		else:
			flag = 'up'
			DFS(y, x, flag, num)

	elif flag == 'up':
		if IsSafe(y+dy[3],x+dx[3]) and data[y+dy[3]][x+dx[3]] == 0:
			data[y+dy[3]][x+dx[3]] = num+1
			DFS(y+dy[3], x+dx[3], flag, num+1)
		else:
			flag = 'right'
			DFS(y, x, flag, num)

for t in range(1,T+1):
	N = int(input())
	data = [[0]*N for _ in range(N)]
	visited = [[0]*N for _ in range(N)]
	dy = [0,1,0,-1] # 우 하 좌 상
	dx = [1,0,-1,0]
	flag = 'right'
	data[0][0] = 1
	DFS(0,0,flag,1)
	print("#{}".format(t))
	for i in data:
		print(*i)
