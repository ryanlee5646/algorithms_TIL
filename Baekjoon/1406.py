'''
L:	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
D:	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
B:	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
P $:	$라는 문자를 커서 왼쪽에 추가함
'''

from sys import stdin
input = stdin.readline

# 1.리스트 풀이(시간초과)
words = list(input().strip())
N = int(input())

now = len(words)

for i in range(N):

  command = input().rstrip().replace(" ", "")
  
  if command[0] == "L":
    if now > 0:
      now -= 1
  elif command[0] == "D":
    if now < len(words):
      now += 1
  elif command[0] == "B":
    if now > 0:
      words.pop(now-1)
      now -= 1
  elif command[0] == "P":
      words.insert(now, command[1])
      now += 1
for i in words:
  print(i, end="")

# 1.리스트 풀이(시간초과)
words = input().strip()
N = int(input())

now = len(words)

for i in range(N):

  command = input().rstrip().replace(" ", "")
  
  if command[0] == "L":
    if now > 0:
      now -= 1
  elif command[0] == "D":
    if now < len(words):
      now += 1
  elif command[0] == "B":
    if now == 0: # 커서 가장 왼쪽이면 패스
      continue
    else:
      words = words[0:now-1] + words[now:]
      now -= 1
  elif command[0] == "P":
      words = words[0:now] + command[1] + words[now:]
      now += 1

print(words)