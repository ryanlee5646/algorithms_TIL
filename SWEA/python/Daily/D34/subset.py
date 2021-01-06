import sys
sys.stdin = open("subset.txt", "r")

def combination(index,combi):
	global count
	if len(combi) == N:
		if sum(combi) == K:
			count+=1
			return
	if index >= len(data):
		return

	elif sum(combi) > K:
		return

	combination(index+1,combi+[data[index]])
	combination(index+1,combi)

T = int(input())
data = [i for i in range(1,13)]

for t in range(1,T+1):
	N, K = map(int,input().split())
	count = 0
	combination(0, [])
	print("#{} {}".format(t,count))
