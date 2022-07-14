# 봄버맨
from copy import deepcopy
from sys import stdin
from collections import deque
input = stdin.readline


# 폭탄 찾기
def find_bomb():
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 'O':
                bomb_loc.append((y, x))
    return


# 모든 칸 폭탄 설치
def install_bomb():
    global graph
    graph = [['O']*M for _ in range(N)]


# 폭탄 폭발
def do_bomb():
    while bomb_loc:
        y, x = bomb_loc.popleft()
        graph[y][x] = '.'
        for j in range(4):
            nx = x+dx[j]
            ny = y+dy[j]
            if 0 <= nx < M and 0 <= ny < N:
                graph[ny][nx] = '.'


N, M, second = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
print(graph)
graph_per_two_second = [['O']*M for _ in range(N)]  # 2초마다 어차피 전체 그래프에 폭탄 설치
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 백트래킹
if second <= 1:  # 주어진 시간이 '1초'면 초기값 출력
    for y in range(N):
        for x in range(M):
            print(graph[y][x], end='')
        print()
elif second % 2 == 0:  # 주어진 시간이 짝수면 모든칸에 'O'을 채워서 출력
    for y in range(N):
        for x in range(M):
            print(graph_per_two_second[y][x], end='')
        print()
else:
    # 1 다음 1초동안 봄버맨은 아무것도 하지 않는다.
    second -= 1
    while second:
        bomb_loc = deque()
        find_bomb()  # 폭탄 좌표 찾기
        install_bomb()  # 모든 칸에 폭탄 설치

        second -= 1  # 2초
        if second == 0:
            break
        do_bomb()  # 폭탄 터트리기 (3초가 되기전에)
        second -= 1  # 3초

    for y in range(N):
        for x in range(M):
            print(graph[y][x], end='')
        print()
