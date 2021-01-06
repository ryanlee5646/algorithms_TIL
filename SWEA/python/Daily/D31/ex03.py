import sys, time
sys.stdin = open("ex03.txt", "r")
stime = time.time()
def cal(robot_permu):
	temp = 0
	for i in range(len(robot_permu)):
		temp += abs(robot_permu[i][0] - snack[i][0]) + abs(robot_permu[i][1] - snack[i][1])
	return temp

def DFS(index,length):
	global low
	if index == length:
		temp_result = cal(robot_permu)
		if low > temp_result:
			low = temp_result
			return
	if len(robot_permu) < length:
		temp_result = cal(robot_permu)
		if temp_result > low:
			return
	for i in range(N):
		if visited[i] == 0:
			visited[i] = 1
			robot_permu.append(robot[i])
			DFS(index+1,length)
			visited[i] = 0
			robot_permu.pop()



T = int(input())
for t in range(1,T+1):
	N = int(input())
	snack_data = list(map(int,input().split()))
	robot_data = list(map(int,input().split()))
	snack = []
	robot = []
	visited = [0] * N
	robot_permu = []
	low = 987654321
	for i in range(0,N*2,2):
		snack.append([snack_data[i],snack_data[i+1]])
		robot.append([robot_data[i], robot_data[i+1]])
	DFS(0,N)
	print("#{} {}".format(t,low))
	print(time.time()-stime)