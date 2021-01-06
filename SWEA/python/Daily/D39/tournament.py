import sys
sys.stdin = open("tournament.txt", "r")

def fight(a,b):
	x = a[1]
	y = b[1]

	if x == y:
		return a
	elif y - x == 1:
		return b
	elif y - x == -1:
		return a
	elif y - x == 2:
		return a
	elif y - x == -2:
		return b


def tournament(now,start,end):
	if len(now) == 1:
		return now[0]
	else:
		# left
		temp_left = now[start:(start+end)//2+1]
		left_start = 0
		left_end = len(temp_left)-1

		a = tournament(temp_left,left_start,left_end)

		# right
		temp_right = now[(start+end)//2+1:end+1]
		right_start = 0
		right_end = len(temp_right) - 1

		b = tournament(temp_right,right_start,right_end)

	return fight(a,b)

T = int(input())

for tc in range(1,T+1):
	n = int(input())

	card = list(map(int,input().split()))

	for i,j in enumerate(card):
	    card[i] = [i+1,j]

	result = tournament(card,0,n-1)

	print(f'#{tc} {result[0]}')
