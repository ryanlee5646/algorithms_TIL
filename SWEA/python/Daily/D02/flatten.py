# 한 쪽 벽면에 다음과 같이 노란색 상자들이 쌓여 있다.
# 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업을 평탄화라고 한다.
# 평탄화를 모두 수행하고 나면, 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내가 된다.
# 평탄화 작업을 위해서 상자를 옮기는 작업 횟수에 제한이 걸려있을 때, 제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환하는 프로그램을 작성하시오.
#
# [제약 사항]
# 가로 길이는 항상 100으로 주어진다.
# 모든 위치에서 상자의 높이는 1이상 100이하로 주어진다.
# 덤프 횟수는 1이상 1000이하로 주어진다.
# 주어진 덤프 횟수 이내에 평탄화가 완료되면 더 이상 덤프를 수행할 수 없으므로 그 때의 최고점과 최저점의 높이 차를 반환한다 (주어진 data에 따라 0 또는 1이 된다).
#
# [입력]
# 총 10개의 테스트 케이스가 주어지며, 각 테스트 케이스의 첫 번째 줄에는 덤프 횟수가 주어진다. 그리고 다음 줄에 각 상자의 높이값이 주어진다.
# [출력]
# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 최고점과 최저점의 높이 차를 출력한다.

# max_height = []
# min_height = []
#
# for t in range(10):
#     num = int(input()) # 덤프 횟수
#     dump_height = list(map(int, input().split()))
#
#     for i in range(num):
#         max_dump = max(dump_height) - 1
#         min_dump = min(dump_height) + 1
#         max_height.append(max_dump)
#         min_height.append(min_dump)
#
#     print(f"#{t+1} {max_height[-1] - min_height[-1]}")

for t in range(1):
    Counts = [0] * 101
    num = int(input()) # 덤프 횟수
    dump_height = list(map(int, input().split())) # 덤프 높이
    start = 1
    end = 100
    for position in dump_height:
        Counts[position] += 1 # 위치별 덤프 높이

    for i in range(num): # 덤프 Counts index 반대로
        while Counts[end] <= 0:
            end -= 1
        while Counts[start] <= 0:
            start += 1

        Counts[end] -= 1
        Counts[end-1] += 1
        Counts[start] -= 1
        Counts[start+1] += 1

        if Counts[end] == 0: # 확실히 0일경우 1을 감소
            end -= 1
        if Counts[start] == 0: #확실히 0일경우 1을 증가
            start += 1

    print(f'#{t+1} {end-start}')


















