# SHOW ME THE DUNGEON
from sys import stdin
input = stdin.readline


def DFS(depth, life, saved_people, path):
    global result
    if life < 0:  # 0보다 작아지는 경우
        return
    if life >= 0:
        result = max(result, saved_people)

    for i in range(monster_num):
        if not visited[i]:
            visited[i] = 1
            DFS(i, life - (sum(monsters[j] for j in path) +
                monsters[i]), saved_people + people[i], path + [i])
            visited[i] = 0


monster_num, life = map(int, input().split())
monsters = list(map(int, input().split()))
people = list(map(int, input().split()))
visited = [0] * monster_num

result = 0

DFS(0, life, 0, [])

print(result)
