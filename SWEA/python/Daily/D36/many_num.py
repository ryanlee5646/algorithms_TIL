import sys
sys.stdin = open("many_num.txt","r")

T = int(input())
for t in range(1,T+1):
	tc = int(input())
	data = list(map(int, input().split()))
	Mymap = [0]*101
	count = 0
	index = 0

	for i in data:
		Mymap[i] += 1

	for j,k in enumerate(Mymap):
		if k >= count:
			count = k
			index = j
	print("#{} {}".format(t,index))