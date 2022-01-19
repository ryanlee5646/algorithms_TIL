# DFS와 BFS

N, line, start = map(int, input().split())

graph = [[] for _ in range(N+1)]

visit = [0] * N+1


print(N)
print(line)
print(start)
print(visit)