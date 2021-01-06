# N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
# M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.
# 다음은 N=5, M=3이고 5개의 숫자 1 2 3 4 5가 배열 v에 들어있는 경우이다.
# 이웃한 M개의 합이 가장 작은 경우 1 + 2 + 3 = 6
# 이웃한 M개의 합이 가장 큰 경우 3 + 4 + 5 = 12
# 답은 12와 6의 차인 6을 출력한다.


T = int(input())
for t in range(T):
    result = []
    N, M = list(map(int, input().split()))  # N = 정수 개수, M = 구간 수
    num_list = list(map(int, input().split()))
    for i in range(M, len(num_list) + 1):
        result.append(sum(num_list[i - M:i]))
    max_num = max(result)
    min_num = min(result)

    print(f"#{t + 1} {max_num - min_num}")
