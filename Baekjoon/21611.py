# 마법사 상어와 블리자드
'''
구현순서
1. 2차원 배열을 딕셔너리를 이용해서 1차원 배열로 구현(좌표:번호 딕셔너리(해시), 번호:좌표 딕셔너리(해시), 인덱스기준으로 구슬숫자 1차원 배열)
2. *구슬 파괴 구현: 상어가 d방향으로 s거리만큼 구슬을 파괴하는거 구현
3. *구슬 이동 구현: 파괴된 구슬기준으로 빈칸이면 번호가 하나 큰 구슬을 빈칸으로 이동한다
4. *구슬 폭발 구현: 4개이상 연속하는 구슬이 있을 때 폭발한다.
5. 폭발한 구슬로 인해 생긴 빈칸 만큼 구슬을 옮긴다. 더이상 폭발하는게 없을 때 까지 반복
6. *구슬변화 구현: 연속하는 구슬을 하나의 그룹으로 봄. 하나의 그룹은 두 개의 구슬 A,B로 변한다.
                  구슬 A번호: 그룹에 들어있는 구슬의 "개수" / 구슬 B번호: 그룹을 이루고 있는 구슬의 "번호" 
                  ex) 2개의 연속하는 1번구슬이 있으면 => A: 2, B: 1
'''

from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
blizards = [list(map(int, input().split())) for _ in range(M)]

location_num = {}  # 좌표:번호
marbles = [-1] * N**2  # 번호 -> 번호에 해당하는 공 번호
result = 0

# 1차원 배열로 초기화


def change_map():
    global num_location, location_num
    # 동 남 서 북 => 끝[0,0]에서부터 동 남 서 북 순서로 들어감
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    start = [0, -1]  # 시작을 (0, -1)로 해서 (0, 0)에서 부터 시작하도록
    cnt = N * N - 1  # 마지막 번호 = N^2-1
    distance = N  # 처음 이동거리 N => 처음에는 한줄 전체, 두번째 부터는 N-1
    flag = 1  # 이동거리 변화 Flag
    direction = 0

    while distance > 0:  # 거리가 0이 되면 종료
        for i in range(distance):
            ny = start[0] + dy[direction]
            nx = start[1] + dx[direction]

            start = (ny, nx)  # 좌표 갱신
            location_num[(ny, nx)] = cnt  # 좌표:번호 ex) { (0,0):48, (0,1):47 ...}
            marbles[cnt] = graph[ny][nx]  # 구슬숫자[번호]
            cnt -= 1

        direction = (direction + 1) % 4  # 방향 변경
        flag += 1
        if flag == 2:  # 방향을 2번 변경하면 distance(이동거리) 1 감소
            flag = 0
            distance -= 1

# 구슬파괴


def destroy(d, s):  # d: 방향 , s: 거리
    dx = [0, 0, 0, -1, 1]  # 상, 하, 좌, 우
    dy = [0, -1, 1, 0, 0]

    shark_x = N//2
    shark_y = N//2

    for i in range(1, s+1):
        nx = shark_x + dx[d] * i
        ny = shark_y + dy[d] * i

        location = location_num[(ny, nx)]  # 좌표값으로 구슬 순번 구하기
        marbles[location] = -1
    return

# 구슬이동


def move():
    global marbles
    blank_cnt = marbles.count(-1)
    marbles = [i for i in marbles if i != -1] + \
        [0] * blank_cnt  # 구슬을 이동시키고 이동시킨 만큼 뒤에 빈칸 추가
    return

# 연속하는 구슬 폭발


def explode():
    global result

    flag = False  # 더이상 파괴될 구슬이 없으면 False 리턴

    cnt = 0  # 연속하는 구슬 개수
    target = 0  # 비교 대상
    marble_num = 0  # 해당 순번에 구슬의 숫자

    for i in range(N*N):  # 0에서 N-1번까지 연속하는 구슬 체크
        if marbles[target] == marbles[i]:
            cnt += 1
        else:  # 연속하지 않는다면
            if cnt >= 4:  # 4개이상 연속하는지 체크
                flag = True
                for j in range(target, i):
                    marbles[j] = -1
                result += marble_num * cnt  # 구슬 숫자 * 개수 추가
            cnt = 1  # i번째 구슬부터 1개로 체크
            target = i  # i번째 부터 체크
            marble_num = marbles[i]  # i번째 구슬 번호 초기화

    return flag

# 구슬 변화


def change():  # A: 구슬의 개수 / B: 구슬의 번호
    global marbles

    tmp_marbles = [0]  # 상어위치 초기화

    group_check = []

    for i in range(1, N*N):
        if not group_check:  # 그룹체크 배열이 비어있으면 하나 추가
            group_check.append(marbles[i])
        elif marbles[i] == group_check[-1]:  # 그룹체크 배열에 있으면 연속하는지 체크
            group_check.append(marbles[i])
        else:  # 연속하지 않는경우
            tmp_marbles.append(len(group_check))  # A: 구슬의 개수
            tmp_marbles.append(group_check[-1])  # B: 구슬의 번호
            group_check = [marbles[i]]  # 현재 구슬 추가

    marbles = [0] * (N*N)
    for i in range(len(tmp_marbles)):
        if i >= (N*N):  # 기존 배열을 넘어서면 break
            break
        marbles[i] = tmp_marbles[i]

    return


def init():

    change_map()  # 1. 맵 초기화(2차원 -> 1차원)

    for d, s in blizards:

        destroy(d, s)  # 2. 방향과 거리를 기준으로 구슬 파괴

        move()  # 3. 빈칸 구슬 이동

        while True:
            if not explode():  # 4-1. 더이상 파괴할 수 없을 때 까지 연속하는 구슬 파괴
                break
            move()  # 4-2 빈칸 구슬 이동

        change()  # 5. 구슬 변화


init()

print(result)
