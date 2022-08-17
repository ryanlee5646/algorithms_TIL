# 요세푸스 문제
'''
1. 종료조건: 배열의 길이가 K보다 같고 큰지 체크
2. 세번째 숫자 pop()하고 result배열에 추가
3. pop한 숫자 다음위치부터 시작해야 하므로 배열을 잘라서 붙여줌
'''
from sys import stdin
import sys
sys.setrecursionlimit(10000)

input = stdin.readline

# 방법 1
# (재귀회수가 백준에서는 1000으로 제한이 있기 때문에 런타임에러 남 재귀회수 늘려주면 통과는 하는데 다른 방법으로 풀어보기)


def josephus(arr):
    global result

    if len(arr) == 0:
        return

    index = K-1
    if index >= len(arr):
        index = index % len(arr)
    result.append(arr.pop(index))
    arr = arr[index:] + arr[:index]
    josephus(arr)


N, K = map(int, input().split())

data = [str(i) for i in range(1, N+1)]

result = []
josephus(data)

print("<", ', '.join(result)[:], ">", sep="")
