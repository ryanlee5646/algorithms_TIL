<<<<<<< HEAD

# tc1
n = 5
clockwise = True

# tc2
# n = 6
# clockwise = False

# tc3
# n = 9
# clockwise = False

def solution(n, clockwise):
    # True: 시계방향 / False: 반시계방향
    return

n = int(input())
clockwise = input()
data = [[0]*n for i in range(n)]
last_num_memo = [0, 1, 1, 3]

for i in range(4, 1000):
    last_num_memo.append(last_num_memo[i-2] + last_num_memo[i-1])
print(last_num_memo)
solution(n, clockwise)
>>>>>>> 896d9eef4c8eb8f5a8c5d3f7ff7829c6cc10292f
