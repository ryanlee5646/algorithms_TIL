# 마법사 상어와 블리자드
# 구현순서
# 1. 2차원 배열을 딕셔너리를 이용해서 1차원 배열로 구현(좌표:번호 딕셔너리(해시), 번호:좌표 딕셔너리(해시), 인덱스기준으로 구슬숫자 1차원 배열)
# 2. *구슬 파괴 구현: 상어가 d방향으로 s거리만큼 구슬을 파괴하는거 구현
# 3. *구슬 이동 구현: 파괴된 구슬기준으로 빈칸이면 번호가 하나 큰 구슬을 빈칸으로 이동한다
# 4. *구슬 폭발 구현: 4개이상 연속하는 구슬이 있을 때 폭발한다.
# 5. 폭발한 구슬로 인해 생긴 빈칸 만큼 구슬을 옮긴다. 더이상 폭발하는게 없을 때 까지 반복
# 6. *구슬변화 구현: 연속하는 구슬을 하나의 그룹으로 봄. 하나의 그룹은 두 개의 구슬 A,B로 변한다.
#                   구슬 A번호: 그룹에 들어있는 구슬의 "개수" / 구슬 B번호: 그룹을 이루고 있는 구슬의 "번호" 
#                   ex) 2개의 연속하는 1번구슬이 있으면 => A: 2, B: 1


from sys import stdin
input = stdin.readline


# n, m = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
# blizards = [list(map(int, input().split())) for _ in range(m)]
# dx = [0, 0, 0, -1, 1] # 위 아래 좌 우
# dy = [0, -1, 1, 0, 0] # 1  2  3  4

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
blizards = [list(map(int, input().split())) for _ in range(M)]

num_location = {} # 번호:좌표
location_num = {} # 좌표:번호
marbles = [-1] * N**2 # 번호 -> 번호에 해당하는 공 번호
result = 0
 
def change_map():
    """
    2차원 좌표 정보를 1차원으로 변경
    :return:
    """
    global num_location, location_num
 
    # 동 남 서 북
    dy_temp = (0, 1, 0, -1)
    dx_temp = (1, 0, -1, 0)
 
    start = (0, -1) # 시작을 (0, -1)로 해서 (0, 0)에서 부터 시작하도록
    cnt = N ** 2 - 1 #  마지막 번호 = N^2-1
    dist =  N # 처음 이동거리 N
    dist_change_flag =  1 # 이동거리 변화 Flag
    dir = 0
 
    while True:
        for i in range(dist):
            ny = loc[0] + dy_temp[dir]
            nx = loc[1] + dx_temp[dir]
 
            loc = (ny, nx) # 좌표 갱신
            n2loc[cnt] = (ny, nx)  # 번호 -> 좌표
            loc2n[(ny, nx)] = cnt # 좌표 -> 번호
            n2ball[cnt] = board[ny][nx] # 번호 -> 구슬 번호
            cnt -= 1
 
        dir = (dir + 1) % 4 # 방향 번경
        dist_change_flag += 1
        if dist_change_flag == 2: # 방향을 2번 변경하면 dist 1 감소
            dist_change_flag = 0
            dist -= 1
 
        if dist == 0: break # 거리가 0이 되면 종료
        
def init():
    # 1. 맵 초기화(2차원 -> 1차원)
    change_map()
    # for d, s in magics:
    #     # 2. 방향과 거리를 기준으로 구슬 파괴
    #     destroy(d, s)
    #     # 3. 파괴된 구슬 정리
    #     arrangement()
    #     # 4. 연속하는 구슬 파괴 및 정리
    #     while True:
    #         if not destroy2(): break
    #         arrangement()
    #     # 5. 구슬 변화
    #     translate_all_balls()
    #     # print_ball()
 
init()
    
# print(result)