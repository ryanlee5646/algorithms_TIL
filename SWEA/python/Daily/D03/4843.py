import sys
sys.stdin = open("4843.txt", "r")

T = int(input())

for t in range(1, T+1):
    num = int(input())
    sort_list =  sorted(list(map(int, input().split())))
    result = []
    
    for i in range(5):
        result.append(sort_list.pop(-1))
        result.append(sort_list.pop(0))
    
    print(f"#{t}", end=' ')
    for j in range(10):
        print(f'{result[j]}', end= " ")
    print()

