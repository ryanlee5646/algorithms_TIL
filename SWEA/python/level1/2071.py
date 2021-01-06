# 10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.
# (소수점 첫째 자리에서 반올림한 정수를 출력한다.)

T = int(input())
result = []
num = []
for i in range(T):
    num = list(map(int, input().split()))
    result.append(round(sum(num)/len(num))) # int하면 소수점 버림, round하면 반올림
for j, n in enumerate(result):
    print(f'#{j+1} {n}')