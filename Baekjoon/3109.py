from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
graph = [input().rstrip() for _ in range(n)]  # rstrip()을 이용해서 개행문자 제거

print(graph)
