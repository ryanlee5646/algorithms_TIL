# 킹과 폰

''' 
1. 킹(흰색)은 판의 아래에서 시작하며 매 차례마다 아래, 위, 대각선 등 총 8 방향으로 한 칸 움직일 수 있다.
2. 폰(검정)은 매 차례마다 아래로 한칸만 움직일 수 있다.
3. 매 차례마다 킹과 폰은 자신의 말을 움직여야한다(두 차례 연속으로 같은 자리에 머물 수 없다.) -> 한 차례는 머물 수 있음, 그리고 다른곳에 갓다가 다시 오는것도 가능

* 킹(흰색)의 승리조건: 폰(검정)을 잡았을 경우
* 폰(검정)의 승리조건: 판의 맨 아래 무사히 도착하면 승리한다.

* 그 밖의 승리조건
1. '금지 칸(F)'과 '위험 칸(D)'이 존재한다. 
금지 칸: 양 쪽 모두가 지나면 안됌

위험 칸: 
1. 오직 폰(검정)만 지나갈 수 있다. 
2. 폰(검정)의 위치에서 왼쪽 아래와 오른쪽 아래에 위치 -> 이 움직이는 위험칸은 판 밖에 벗어나거나, 금지 칸과 겹치지 않는 이상 유효하다.

*** 게임승리조건 ***
1. 킹(흰색)이 폰(검정)의 좌표로 올라가 폰을 잡을 경우 -> 킹(흰색) 승리
2. 킹(흰색)이 움직여야할 차례지만 갈 수 있는 열린 칸이 없는 경우 -> 폰(검정) 승리
3. 폰(검정)이 움직여야 하는데 열린 칸 혹은 위험 칸으로 움직일 수 없는 경우 ->
4. 폰이 체스 판의 맨 밑에 칸에 위치할 경우 -> 폰(검정)의 승리
5. 4번의 조건이 아닌 경우 -> 킹(흰색)의 승리

게임의 선공은 항상 흰색 킹, 

# 구현
1. 

'''
from sys import stdin
from collections import deque

input = stdin.readline

T =  int(input())

dir_x = [0,1,1,1,0,-1,-1,-1] # 시계방향 12시부터
dir_y = [-1,-1,0,1,1,1,0,-1]

def BFS(x,y,turn):

  queue = deque()
  queue.append((x,y,turn))
  visited[king_y][king_x][0] = True
  
  while queue:
    now_x, now_y, now_turn = queue.popleft()

    if graph[pon_y + now_turn][pon_x] == 'F': # 검은색 다음구역이 금지구역
      return True
    
    if pon_x + now_turn > 7: # 폰이 밑에 도달했을 경우
      return False
    
    for i in range(8):
      dx = now_x + dir_x[i]
      dy = now_y + dir_y[i]
      next_turn = now_turn +1
      
      if is_possible(dx, dy) and is_go(dx, dy) and is_visit(dx, dy, next_turn):
        if not pon_dangerous(dx, dy, next_turn):
          visited[dx][dy][next_turn] = True

          if catch_pon(dx, dy, now_turn):
            return True
          
          queue.append((dx, dy, next_turn))
          
def is_possible(x, y): # 좌표를 벗어나지 않는지 체크
    if 0 <= x < 8 and 0 <= y < 8:
      return True
    return False

def is_go(x,y): # 위험 칸 혹은 금지칸이 아닌지 체크
  if graph[y][x] != 'F' and graph[y][x] != 'D':
    return True
  return False

def is_visit(x, y, turn): # 방문한적이 있는지 체크
  if visited[y][x][turn] == True:
    return False
  return True

def pon_dangerous(x, y, turn): # 폰의 위험 칸인지 체크
  if (y == pon_y + turn and x == pon_x -1) or (y == pon_y + turn and pon_x +1):
    return True
  return False

def catch_pon(x, y, turn): # 폰이 있는지 체크
  if (y == pon_y + turn and x == pon_x):
    return True
  return False 
     
for t in range(T):
  graph = [list(input().rstrip()) for _ in range(8)]

  king_x, king_y = map(int, input().split())
  king_x, king_y = king_x-1, 8-king_y
  pon_x, pon_y = map(int, input().split())
  pon_x, pon_y = pon_x-1, 8-pon_y
  
  visited = [[[False] * 8 for _  in range(8)] for _ in range(8)]
  
  result = BFS(king_x, king_y, 0)
  if result:
    print('White')
  else:
    print('Black')



'''
# 0 (시작)
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . P . .
. . . . D . D .
. . K . . . . .

# 1
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. K K K . p . .
. K . K D . D .

# 3
. . . . . . . .
. . . . . . . .
. . . . . . . .
K K K K K . . .
K . . . K . . .
K . . K . P . .

'''