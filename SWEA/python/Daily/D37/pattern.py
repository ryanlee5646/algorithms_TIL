import sys
sys.stdin = open("pattern.txt","r")

T = int(input())
for t in range(1,T+1):
	data = input()
	result = 0
	for i in range(1,11):
		if data[:i] == data[i:2*i]:
			result = i
			break
	print("#{} {}".format(t,i))



