'''
* push X: 정수 X를 큐에 넣는 연산이다.
* pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
* size: 큐에 들어있는 정수의 개수를 출력한다.
* empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
* front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
* back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
from sys import stdin

input = stdin.readline

N = int(input())
queue = []
for _ in range(N):
  command = list(map(str, input().split()))
  
  if command[0] == 'push':
    queue.append(command[1])

  elif command[0] == 'pop':
    if queue:
      print(queue.pop(0))
    else:
      print(-1)
  elif command[0] == 'size':
    print(len(queue))
  elif command[0] == 'empty':
    if queue:
      print(0)
    else:
      print(1)
  elif command[0] == 'front':
    if queue:
      print(queue[0])
    else:
      print(-1)
  elif command[0] == 'back':
    if queue:
      print(queue[-1])
    else:
      print(-1)