import sys
sys.stdin = open("num_arrange.txt", "r")

T = int(input())
for t in range(1,T+1):
	N = int(input())
	data = list(map(int, input().split()))
	data.sort()
	print("#{} ".format(t))
	for i in data:
		print("{}".format(i), end=' ')
	print()