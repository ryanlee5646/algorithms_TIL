import sys
sys.stdin = open("best_distance.txt","r")

T = int(input())
def cal(lst):
    temp_list = [start] + result + [end]
    temp = 0
    for i in range(1, len(temp_list)):
        temp += (abs(temp_list[i - 1][0] - temp_list[i][0]) + abs(temp_list[i - 1][1] - temp_list[i][1]))
    return temp
def Back(here):
    global result, low
    if len(result) == N:
        tmp_result = cal(result)
        if tmp_result >= low:
            return
        else:
            low = tmp_result
    if len(result) >= 1:
        print(result)
        tmp_result = cal(result)
        if tmp_result >= low: # 첫번째 돌때 low 초기값보다 클 순 없음.
            return
    for i in range(len(route)):
        if not visited[i]:
            visited[i] = 1
            result.append(route[i])
            Back(here+1)
            visited[i] = 0
            result.pop()
for t in range(1,T+1):
    N = int(input())
    people = list(map(int,input().split()))
    start = [people.pop(0),people.pop(0)]
    end = [people.pop(0), people.pop(0)]
    route = [[people[i],people[i+1]] for i in range(0,len(people),2)]
    visited = [0]*N
    result = []
    low = 987654321

    Back(0)
    print("#{} {}".format(t,low))


# T = int(input())
#
# def Back(here):
#     global result, low
#     if len(result) == N:
#         temp_list = [start] + result + [end]
#         temp = 0
#         for i in range(1, len(temp_list)):
#             temp += (abs(temp_list[i - 1][0] - temp_list[i][0]) + abs(temp_list[i - 1][1] - temp_list[i][1]))
#         if temp >= low:
#             return
#         else:
#             low = temp
#     if len(result) >= 1:
#         temp_list = [start] + result + [end]
#         temp = 0
#         for i in range(1, len(temp_list)):
#             temp += (abs(temp_list[i - 1][0] - temp_list[i][0]) + abs(temp_list[i - 1][1] - temp_list[i][1]))
#         if temp >= low:
#             return
#     for i in range(len(route)):
#         if not visited[i]:
#             visited[i] = 1
#             result.append(route[i])
#             Back(here+1)
#             visited[i] = 0
#             result.pop()
# for t in range(1,T+1):
#     N = int(input())
#     people = list(map(int,input().split()))
#     start = [people.pop(0),people.pop(0)]
#     end = [people.pop(0), people.pop(0)]
#     route = [[people[i],people[i+1]] for i in range(0,len(people),2)]
#     visited = [0]*N
#     result = []
#     low = 987654321
#
#     Back(0)
#     print("#{} {}".format(t,low))























# def cal(lst):       # list 를 인자로 받으며 회사 , 집까지 고려해 거리 반환
#     tmp = starte + route + end
#     tmpsum = 0
#     for i in range(1, len(tmp)):
#         tmpsum += (abs(tmp[i][0] - tmp[i - 1][0]) + abs(tmp[i][1] - tmp[i - 1][1]))
#     return tmpsum
# def Backtrack(start):
#     global low
#     if len(route) == N:     #개수가 N개이면 무조건 계산
#         tmpresult = cal(route)
#         if tmpresult <low:
#             low = tmpresult
#
#     if len(route) >= 1 :    #초기값이 9876...이 아니면(계산이 한번됬으면)계산
#         tmpresult = cal(route)
#         if tmpresult>=low:      #중간 계산 결과가 결과 값보다 크면 리턴 후속작업 안함
#             return
#     for i in range(len(people)):
#         if not visited[i]:
#             visited[i] = 1
#             route.append(people[i])
#             Backtrack(start+1)
#             visited[i] = 0
#             route.pop()
# T = int(input())
#
# for t in range(1,T+1):
#     N = int(input())
#     data = list(map(int, input().split()))
#     people = []  #고객 좌표
#     route = []
#     starte = [[data[0],data[1]]]
#     end = [[data[2],data[3]]]
#     visited = [0] * N
#     low = 987654321
#      #이동경로를 담을 리스트
#     for i in range(4,(N+2)*2,2):
#         people.append([data[i],data[i+1]])
#
#
#     Backtrack(0)
#     print("#{} {}".format(t,low))





