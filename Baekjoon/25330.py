# SHOW ME THE DUNGEON
from sys import stdin
input = stdin.readline

def DFS(depth, life, saved_people):
  global result
  if life <= 0:
    if result < saved_people:
      result = saved_people
      return
  for i in range(monster_num):
    visited[i] = 1
    DFS(i+1, life-monsters[i], saved_people+ people[i])  
    visited[i] = 0
  
  return

monster_num, life = map(int, input().split())
monsters = list(map(int, input().split()))
people = list(map(int, input().split()))
visited = [0] * monster_num

result = 0


DFS(0, life, 0)

print(result)