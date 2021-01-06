import sys,time
sys.stdin = open("ex03.txt", "r")
stime = time.time()
def cal(snack_per):
    temp = 0
    for i in range(len(snack_per)):
        temp += abs(robot[i][0]-snack_per[i][0]) + abs(robot[i][1]-snack_per[i][1])
    return temp

def permutation(index, length):
    global low
    if len(snack_per) == length:
        temp_result = cal(snack_per)
        if temp_result < low:
            low = temp_result
            return
    if len(snack_per) < length:
        temp_result = cal(snack_per)
        if temp_result > low:
            return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            snack_per.append(snack[i])
            permutation(index+1, length)
            visited[i] = 0
            snack_per.pop()

T = int(input())
for t in range(1,T+1):
    N = int(input())
    robot_data = list(map(int, input().split()))
    snack_data = list(map(int, input().split()))
    robot = []
    snack = []
    visited = [0] * N
    snack_per = []
    low = 987654321
    temp = 0
    for i in range(0,N*2,2):
        robot.append([robot_data[i], robot_data[i+1]])
        snack.append([snack_data[i], snack_data[i+1]])
    permutation(0, len(snack))
    print("#{} {}".format(t,low))
    print(time.time() - stime)

